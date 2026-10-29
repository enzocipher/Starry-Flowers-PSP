"""Check prepared pixels, tile geometry and the normal PSP package against source art."""
import io
import json
import pathlib
import struct
import hashlib
from PIL import Image
import pycdlib
from psp_textures import decode_dxt5
from psp_pipeline import validate_manifest

root = pathlib.Path(__file__).resolve().parents[1]
dist = root / "psp/dist"
manifest = json.loads((dist / "DATA/MANIFEST.JSON").read_text(encoding="utf-8"))
validate_manifest(manifest, dist / "DATA")
story = json.loads((root / "story.json").read_text(encoding="utf-8"))
sources = dict(story["images"])
sources.update({"ui " + n: "gui/" + n + ".png" for n in ["main_menu", "game_menu", "textbox", "nvl"]})
checked = set()
worst_error = 0.
mipmaps_checked = 0
for name, info in manifest["images"].items():
    original = Image.open(root / "assets" / sources[name]).convert("RGBA")
    original = original.resize((info["raster_width"], info["raster_height"]), Image.Resampling.LANCZOS)
    levels = [original] + [original.resize((max(1, (original.width + (1 << level) - 1) // (1 << level)), max(1, (original.height + (1 << level) - 1) // (1 << level))), Image.Resampling.LANCZOS) for level in (1, 2)]
    for tile in info["tiles"]:
        if tile["file"] in checked:
            continue
        tw, th = tile["texture_width"], tile["texture_height"]
        data = (dist / "DATA" / tile["file"]).read_bytes()
        dxt5 = tile.get("dxt5", False)
        assert len(data) == tw * th * (1 if dxt5 else 4) * 21 // 16
        x, y, w, h = (tile[k] for k in ["x", "y", "width", "height"])
        offset = 0
        for level, source in enumerate(levels):
            scale = 1 << level
            mw, mh = tw // scale, th // scale
            length = mw * mh * (1 if dxt5 else 4)
            pixels = decode_dxt5(data[offset:offset + length], mw, mh) if dxt5 else Image.frombytes("RGBA", (mw, mh), data[offset:offset + length])
            offset += length
            expected = source.crop(((x - 4) // scale, (y - 4) // scale, (x - 4 + tw) // scale, (y - 4 + th) // scale))
            inset = 4 // scale
            # Check the visible region at every level, excluding the gutter.
            bounds = (inset, inset, inset + w // scale, inset + h // scale)
            actual = pixels.crop(bounds)
            expected = expected.crop(bounds)
            if dxt5:
                from PIL import ImageChops, ImageStat
                error = sum(ImageStat.Stat(ImageChops.difference(actual.convert("RGBa"), expected.convert("RGBa"))).mean) / 4
                worst_error = max(worst_error, error)
                assert error < 12., (name, level, error)
            else:
                assert actual.tobytes() == expected.tobytes()
            mipmaps_checked += 1
        assert x + w <= original.width and y + h <= original.height
        checked.add(tile["file"])

iso = pycdlib.PyCdlib()
iso.open(str(dist / "StarryFlowers.iso"))
def read_iso(path):
    with iso.open_file_from_iso(iso_path=path + ";1") as stream:
        return stream.read()
prx = (root / "psp/target/mipsel-sony-psp/release/starryflowers-psp.prx").read_bytes()
assert read_iso("/PSP_GAME/SYSDIR/EBOOT.BIN") == prx
for name in manifest["files"]:
    with (dist / "DATA" / name).open("rb") as local:
        expected = hashlib.file_digest(local, "sha256").digest()
    with iso.open_file_from_iso(iso_path="/PSP_GAME/USRDIR/DATA/" + name + ";1") as packed_file:
        assert hashlib.file_digest(packed_file, "sha256").digest() == expected, ("ISO resource mismatch", name)
try:
    read_iso("/PSP_GAME/USRDIR/DATA/AUDIT")
except pycdlib.pycdlibexception.PyCdlibInvalidInput:
    pass
else:
    raise AssertionError("Normal ISO contains the audit marker")
for name, size in [("ICON0.PNG", (144, 80)), ("PIC1.PNG", (480, 272))]:
    assert Image.open(io.BytesIO(read_iso("/PSP_GAME/" + name))).size == size
iso.close()
packed = (dist / "EBOOT.PBP").read_bytes()
offsets = list(struct.unpack_from("<8I", packed, 8)) + [len(packed)]
assert packed[offsets[6]:offsets[7]] == prx
for index, size in [(1, (144, 80)), (4, (480, 272))]:
    assert Image.open(io.BytesIO(packed[offsets[index]:offsets[index + 1]])).size == size
print(f"Verified {len(checked)} source tiles, {mipmaps_checked} mip levels, {len(manifest['files'])} ISO resources, ISO/PBP executables and launcher art; worst premultiplied DXT5 error {worst_error:.3f}/255.")
