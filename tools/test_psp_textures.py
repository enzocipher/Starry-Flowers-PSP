import unittest
from psp_textures import psp_blocks, encode_dxt5, decode_dxt5, encode_texture
from PIL import Image

class TextureTests(unittest.TestCase):
    @staticmethod
    def _levels(middle):
        images = [Image.new("RGBA", (16, 16), "white"), middle, Image.new("RGBA", (4, 4), "white")]
        return [(image, (0, 0, image.width, image.height)) for image in images]

    @staticmethod
    def _checker(alpha=255):
        image = Image.new("RGBA", (8, 8))
        colors = [(255, 0, 0, alpha), (0, 255, 0, alpha), (0, 0, 255, alpha), (255, 255, 255, alpha)]
        image.putdata([colors[(y % 2) * 2 + x % 2] for y in range(8) for x in range(8)])
        return image

    def test_white_mip_chain_uses_dxt5(self):
        data, dxt5 = encode_texture(self._levels(Image.new("RGBA", (8, 8), "white")))
        self.assertTrue(dxt5)
        self.assertEqual(len(data), 336)

    def test_visible_mip_error_falls_back_to_rgba(self):
        levels = self._levels(self._checker())
        data, dxt5 = encode_texture(levels, max_error=0.01)
        self.assertFalse(dxt5)
        self.assertEqual(data, b"".join(image.tobytes() for image, _ in levels))
        self.assertEqual(len(data), 1344)

    def test_transparent_rgb_does_not_count_towards_error(self):
        data, dxt5 = encode_texture(self._levels(self._checker(alpha=0)), max_error=0.01)
        self.assertTrue(dxt5)
        self.assertEqual(len(data), 336)

    def test_ge_alpha_indices_are_little_endian_48_bits(self):
        pc = bytes(range(16))
        ge = psp_blocks(pc)
        self.assertEqual(ge[:8], bytes([12, 13, 14, 15, 8, 9, 10, 11]))
        self.assertEqual(int.from_bytes(ge[8:14], "little"), int.from_bytes(pc[2:8], "little"))
        self.assertEqual(ge[14:16], pc[:2])

    def test_transparency_survives_compression(self):
        source = Image.new("RGBA", (16, 16))
        source.putdata([(160, 80, 200, x * 17) for y in range(16) for x in range(16)])
        decoded = decode_dxt5(encode_dxt5(source), 16, 16)
        # BC3 interpolates alpha using six intermediate values per block.
        self.assertLessEqual(max(abs(a[3] - b[3]) for a, b in zip(source.getdata(), decoded.getdata())), 12)
        self.assertEqual(decoded.getpixel((0, 0))[3], 0)
        self.assertEqual(decoded.getpixel((15, 0))[3], 255)

    def test_thin_edge_block_preserves_high_alpha_transition(self):
        source = Image.new("RGBA", (4, 4), (180, 110, 60, 0))
        for y, alpha in enumerate([254, 172, 46, 0]):
            for x in range(4):
                source.putpixel((x, y), (180, 110, 60, alpha))
        decoded = decode_dxt5(encode_dxt5(source), 4, 4)
        errors = [abs(source.getpixel((x, y))[3] - decoded.getpixel((x, y))[3]) for y in range(4) for x in range(4)]
        self.assertLessEqual(max(errors), 10)

if __name__ == "__main__":
    unittest.main()
