"""BC3 textures in the PSP GE block order, retaining the source alpha channel."""
import io
import struct
from PIL import Image, ImageChops, ImageStat


def _alpha_palette(endpoint0, endpoint1):
    if endpoint0 > endpoint1:
        return [endpoint0, endpoint1] + [((7 - i) * endpoint0 + i * endpoint1) // 7 for i in range(1, 7)]
    return [endpoint0, endpoint1] + [((5 - i) * endpoint0 + i * endpoint1) // 5 for i in range(1, 5)] + [0, 255]


def _alpha_indices(values, palette):
    indices = [min(range(8), key=lambda index: (abs(values[pixel] - palette[index]), index)) for pixel in range(16)]
    error = sum((values[pixel] - palette[indices[pixel]]) ** 2 for pixel in range(16))
    packed = sum(index << (pixel * 3) for pixel, index in enumerate(indices)).to_bytes(6, "little")
    return error, packed


def _improve_small_alpha_blocks(encoded, image):
    """Repair Pillow's poor BC3 alpha indices on thin edge tiles without touching color data."""
    width, height = image.size
    if width > 32 and height > 32:
        return
    alpha = image.convert("RGBA").getchannel("A").tobytes()
    block_number = 0
    for block_y in range(0, height, 4):
        for block_x in range(0, width, 4):
            values = [alpha[(block_y + dy) * width + block_x + dx] for dy in range(4) for dx in range(4)]
            if min(values) == max(values):
                block_number += 1
                continue
            offset = block_number * 16
            block = encoded[offset:offset + 16]
            endpoint0, endpoint1 = block[14], block[15]
            current_palette = _alpha_palette(endpoint0, endpoint1)
            current_indices = int.from_bytes(block[8:14], "little")
            current_error = sum((value - current_palette[(current_indices >> (pixel * 3)) & 7]) ** 2
                                for pixel, value in enumerate(values))
            high, low = max(values), min(values)
            candidate_palette = _alpha_palette(high, low)
            candidate_error, candidate_indices = _alpha_indices(values, candidate_palette)
            if candidate_error < current_error:
                encoded[offset + 8:offset + 14] = candidate_indices
                encoded[offset + 14:offset + 16] = bytes((high, low))
            block_number += 1

# PC: alpha endpoints, alpha indices, colour endpoints, colour indices.
# GE: colour indices, colour endpoints, 48-bit alpha indices, alpha endpoints.
def psp_blocks(source):
    result = bytearray()
    for offset in range(0, len(source), 16):
        block = source[offset:offset + 16]
        result.extend(block[12:16] + block[8:12] + block[2:8] + block[:2])
    return result

def encode_dxt5(image):
    stream = io.BytesIO()
    image.save(stream, format="DDS", pixel_format="DXT5")
    source = stream.getvalue()[128:]
    result = psp_blocks(source)
    _improve_small_alpha_blocks(result, image)
    assert len(result) == image.width * image.height
    return result

def decode_dxt5(data, width, height):
    source = bytearray()
    for offset in range(0, len(data), 16):
        block = data[offset:offset + 16]
        source.extend(block[14:16] + block[8:14] + block[4:8] + block[:4])
    header = b"DDS " + struct.pack("<7I", 124, 0x81007, height, width, width * height, 0, 0)
    header += bytes(44) + struct.pack("<II4sIIIII", 32, 4, b"DXT5", 0, 0, 0, 0, 0)
    header += struct.pack("<5I", 0x1000, 0, 0, 0, 0)
    return Image.open(io.BytesIO(header + source)).convert("RGBA")


def encode_texture(levels, max_error=12.0):
    """Keep all mip levels lossless if any visible level compresses poorly.

    Each entry is (RGBA image including its gutter, visible crop bounds).
    The GE texture format applies to the whole chain, so fallback includes
    every level. Both formats are already supported by the native renderer.
    """
    encoded = []
    for image, bounds in levels:
        data = encode_dxt5(image)
        decoded = decode_dxt5(data, image.width, image.height)
        expected = image.crop(bounds).convert("RGBa")
        actual = decoded.crop(bounds).convert("RGBa")
        error = sum(ImageStat.Stat(ImageChops.difference(actual, expected)).mean) / 4
        if error >= max_error:
            return b"".join(image.convert("RGBA").tobytes() for image, _ in levels), False
        encoded.append(data)
    return b"".join(encoded), True
