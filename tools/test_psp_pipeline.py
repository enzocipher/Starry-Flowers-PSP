import pathlib
import struct
import tempfile
import unittest

from psp_pipeline import (
    cached_image_descriptor,
    cleanup_obsolete,
    convert_audio_cached,
    find_matching_pbp,
    load_valid_manifest,
    pbp_executable,
    unique_audio_stems,
    validate_manifest,
)


def make_pbp(executable: bytes) -> bytes:
    offsets = [40] * 7 + [40 + len(executable)]
    return b"\x00PBP" + struct.pack("<I8I", 0x00010000, *offsets) + executable


class PspPipelineTests(unittest.TestCase):
    def test_image_cache_checks_full_rgba_mip_chain(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            tile = root / "RGBA.TEX"
            tile.write_bytes(bytes(1344))
            descriptor = {"tiles": [{"file": tile.name, "texture_width": 16, "texture_height": 16, "dxt5": False}], "_cache": {"source_sha256": "hash", "recipe": "rgba"}}
            previous = {"images": {"scene": descriptor}}
            self.assertIs(cached_image_descriptor(previous, "scene", "hash", "rgba", root), descriptor)
            tile.write_bytes(bytes(336))
            self.assertIsNone(cached_image_descriptor(previous, "scene", "hash", "rgba", root))

    def test_validate_manifest_accepts_listed_references(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = pathlib.Path(temp_dir)
            for filename in ("MANIFEST.JSON", "KEEP.TEX", "FONT.RAW", "SOUND.PCM"):
                (directory / filename).touch()
            manifest = {
                "files": ["MANIFEST.JSON", "KEEP.TEX", "FONT.RAW", "SOUND.PCM"],
                "images": {"scene": {"tiles": [{"file": "KEEP.TEX"}]}},
                "fonts": {"12": {"glyphs": {"a": {"file": "FONT.RAW"}}}},
                "audio": {"track": "SOUND.PCM"},
            }
            validate_manifest(manifest, directory)

    def test_validate_manifest_rejects_unlisted_references(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = pathlib.Path(temp_dir)
            (directory / "MANIFEST.JSON").touch()
            (directory / "MISSING").touch()
            cases = {
                "tile": {"images": {"scene": {"tiles": [{"file": "MISSING"}]}}},
                "font": {"fonts": {"12": {"glyphs": {"a": {"file": "MISSING"}}}}},
                "audio": {"audio": {"track": "MISSING"}},
            }
            for kind, references in cases.items():
                with self.subTest(kind=kind):
                    with self.assertRaisesRegex(ValueError, "referenciados"):
                        validate_manifest({"files": ["MANIFEST.JSON"], **references}, directory)

    def test_audio_cache_keys_source_and_config_and_publishes_atomically(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            source = root / "music.ogg"
            source.write_bytes(b"source one")
            target = root / "music.pcm"
            calls = []

            def fake_ffmpeg(args, check):
                calls.append(args)
                pcm = b"pcm:" + source.read_bytes()
                pcm += b"\0" * (-len(pcm) % 4)
                pathlib.Path(args[-1]).write_bytes(pcm)

            record, hit = convert_audio_cached(source, target, "hash-one", None, "ffmpeg", fake_ffmpeg)
            self.assertFalse(hit)
            self.assertEqual(target.read_bytes(), b"pcm:source one\0\0")
            _, hit = convert_audio_cached(source, target, "hash-one", record, "ffmpeg", fake_ffmpeg)
            self.assertTrue(hit)
            self.assertEqual(len(calls), 1)

            source.write_bytes(b"source two")
            changed, hit = convert_audio_cached(source, target, "hash-two", record, "ffmpeg", fake_ffmpeg)
            self.assertFalse(hit)
            self.assertEqual(target.read_bytes(), b"pcm:source two\0\0")
            self.assertEqual(len(calls), 2)

            def failed_ffmpeg(args, check):
                pathlib.Path(args[-1]).write_bytes(b"partial")
                raise RuntimeError("conversion failed")

            with self.assertRaises(RuntimeError):
                convert_audio_cached(source, target, "hash-three", changed, "ffmpeg", failed_ffmpeg)
            self.assertEqual(target.read_bytes(), b"pcm:source two\0\0")

    def test_duplicate_audio_stems_are_rejected_case_insensitively(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            with self.assertRaisesRegex(ValueError, "duplicados"):
                unique_audio_stems([root / "Theme.ogg", root / "theme.wav"])

    def test_audio_cache_reconverts_empty_or_misaligned_pcm(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            source = root / "music.ogg"
            source.write_bytes(b"source")
            target = root / "music.pcm"
            calls = []

            def fake_ffmpeg(args, check):
                calls.append(args)
                pathlib.Path(args[-1]).write_bytes(bytes(8))

            record, _ = convert_audio_cached(source, target, "same-hash", None, "ffmpeg", fake_ffmpeg)
            self.assertEqual(len(calls), 1)
            target.write_bytes(b"")
            _, hit = convert_audio_cached(source, target, "same-hash", record, "ffmpeg", fake_ffmpeg)
            self.assertFalse(hit)
            self.assertEqual(len(calls), 2)
            target.write_bytes(b"bad")
            _, hit = convert_audio_cached(source, target, "same-hash", record, "ffmpeg", fake_ffmpeg)
            self.assertFalse(hit)
            self.assertEqual(len(calls), 3)
            self.assertEqual(target.stat().st_size, 8)

    def test_image_cache_requires_matching_source_recipe_and_existing_tiles(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            tile = root / "TILE.TEX"
            tile.write_bytes(bytes(16 * 16 + 8 * 8 + 4 * 4))
            descriptor = {"tiles": [{"file": tile.name, "texture_width": 16, "texture_height": 16, "dxt5": True}], "_cache": {"source_sha256": "hash-a", "recipe": "recipe-1"}}
            previous = {"images": {"scene": descriptor}}
            self.assertIs(cached_image_descriptor(previous, "scene", "hash-a", "recipe-1", root), descriptor)
            self.assertIsNone(cached_image_descriptor(previous, "scene", "hash-b", "recipe-1", root))
            self.assertIsNone(cached_image_descriptor(previous, "scene", "hash-a", "recipe-2", root))
            tile.write_bytes(b"truncated")
            self.assertIsNone(cached_image_descriptor(previous, "scene", "hash-a", "recipe-1", root))
            tile.write_bytes(bytes(16 * 16 + 8 * 8 + 4 * 4))
            tile.unlink()
            self.assertIsNone(cached_image_descriptor(previous, "scene", "hash-a", "recipe-1", root))

    def test_cleanup_deletes_only_previous_manifest_outputs_after_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            for name in ("MANIFEST.JSON", "old.TEX", "keep.bin", "new.TEX"):
                (root / name).write_bytes(b"x")
            previous = {"files": ["MANIFEST.JSON", "old.TEX"]}
            current = {"files": ["MANIFEST.JSON", "new.TEX"]}
            removed = cleanup_obsolete(previous, current, root)
            self.assertEqual(removed, ["old.TEX"])
            self.assertFalse((root / "old.TEX").exists())
            self.assertTrue((root / "keep.bin").exists())

    def test_cleanup_refuses_incomplete_new_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            (root / "old.TEX").write_bytes(b"x")
            with self.assertRaisesRegex(ValueError, "Faltan"):
                cleanup_obsolete({"files": ["MANIFEST.JSON", "old.TEX"]}, {"files": ["MANIFEST.JSON", "missing.TEX"]}, root)
            self.assertTrue((root / "old.TEX").exists())

    def test_invalid_previous_manifest_is_never_used_for_cleanup(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            (root / "old.TEX").write_bytes(b"x")
            (root / "MANIFEST.JSON").write_text('{"files":["../outside"]}', encoding="utf-8")
            self.assertIsNone(load_valid_manifest(root))

    def test_pbp_must_embed_the_exact_prx_payload(self):
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            matching = root / "goodEBOOT.PBP"
            stale = root / "staleEBOOT.PBP"
            matching.write_bytes(make_pbp(b"same executable"))
            stale.write_bytes(make_pbp(b"different executable"))
            self.assertEqual(pbp_executable(matching.read_bytes()), b"same executable")
            self.assertEqual(find_matching_pbp([stale, matching], b"same executable"), matching)
            self.assertIsNone(find_matching_pbp([stale], b"same executable"))

    def test_empty_data_psp_does_not_consume_psar_as_executable(self):
        offsets = [40] * 8
        data = b"\x00PBP" + struct.pack("<I8I", 0x00010000, *offsets) + b"PSAR data"
        with self.assertRaisesRegex(ValueError, "DATA.PSP"):
            pbp_executable(data)


if __name__ == "__main__":
    unittest.main()
