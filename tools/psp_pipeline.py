"""Small, filesystem-safe helpers shared by PSP preparation and packaging."""
from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import struct
import subprocess
import tempfile
from typing import Callable, Iterable


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_write(path: pathlib.Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as output:
            output.write(data)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def atomic_json(path: pathlib.Path, value: object) -> None:
    atomic_write(path, json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


def load_valid_manifest(directory: pathlib.Path) -> dict | None:
    """Accept only a complete manifest whose file list stays inside this directory."""
    path = directory / "MANIFEST.JSON"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
        names = manifest["files"]
        if not isinstance(names, list) or not names or "MANIFEST.JSON" not in names:
            return None
        if any(not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+", name) for name in names):
            return None
        if len(set(names)) != len(names):
            return None
        if any(not (directory / name).is_file() for name in names):
            return None
        return manifest
    except (OSError, ValueError, KeyError, TypeError):
        return None


def validate_manifest(manifest: dict, directory: pathlib.Path) -> None:
    names = manifest.get("files")
    if not isinstance(names, list) or not names or "MANIFEST.JSON" not in names:
        raise ValueError("El manifiesto generado no contiene una lista de archivos válida")
    if any(not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+", name) for name in names):
        raise ValueError("El manifiesto generado contiene nombres de archivo inseguros")
    if len(set(names)) != len(names):
        raise ValueError("El manifiesto generado contiene archivos duplicados")
    referenced = {
        tile["file"]
        for image in manifest.get("images", {}).values()
        for tile in image["tiles"]
    }
    referenced.update(
        glyph["file"]
        for font in manifest.get("fonts", {}).values()
        for glyph in font["glyphs"].values()
    )
    referenced.update(manifest.get("audio", {}).values())
    unlisted = referenced.difference(names)
    if unlisted:
        raise ValueError("Archivos referenciados ausentes de la lista: " + ", ".join(sorted(unlisted)[:8]))
    missing = [name for name in names if name != "MANIFEST.JSON" and not (directory / name).is_file()]
    if missing:
        raise ValueError("Faltan archivos generados del manifiesto: " + ", ".join(missing[:8]))


def cleanup_obsolete(previous: dict | None, current: dict, directory: pathlib.Path) -> list[str]:
    """Remove only files claimed by the previous valid manifest after the new one validates."""
    validate_manifest(current, directory)
    if previous is None:
        return []
    current_names = set(current["files"])
    removed = []
    for name in previous["files"]:
        if name == "MANIFEST.JSON" or name in current_names:
            continue
        target = directory / name
        if target.is_file():
            target.unlink()
            removed.append(name)
    return removed


def convert_audio_cached(
    source: pathlib.Path,
    destination: pathlib.Path,
    source_hash: str,
    cached: dict | None,
    ffmpeg: str,
    runner: Callable = subprocess.run,
    config: str = "ffmpeg:s16le:stereo:44100:v1",
) -> tuple[dict, bool]:
    """Reuse an exact source/config result, otherwise convert to a temp file and atomically publish."""
    if (cached and cached.get("source_sha256") == source_hash and cached.get("config") == config
            and cached.get("file") == destination.name and destination.is_file()
            and destination.stat().st_size > 0 and destination.stat().st_size % 4 == 0):
        return cached, True
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{destination.stem}.", suffix=".pcm.tmp", dir=destination.parent)
    os.close(fd)
    try:
        runner([ffmpeg, "-v", "error", "-y", "-i", str(source), "-f", "s16le", "-ac", "2", "-ar", "44100", temporary], check=True)
        if not pathlib.Path(temporary).is_file() or pathlib.Path(temporary).stat().st_size == 0 or pathlib.Path(temporary).stat().st_size % 4:
            raise RuntimeError(f"La conversión de audio no produjo PCM estéreo de 16 bits válido: {source}")
        os.replace(temporary, destination)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
    return {"source_sha256": source_hash, "config": config, "file": destination.name}, False


def unique_audio_stems(paths: Iterable[pathlib.Path]) -> list[pathlib.Path]:
    seen: dict[str, pathlib.Path] = {}
    result = []
    for path in sorted(paths):
        key = path.stem.casefold()
        if key in seen:
            raise ValueError(f"Stems de audio duplicados: {seen[key].name} y {path.name}")
        seen[key] = path
        result.append(path)
    return result


def cached_image_descriptor(previous: dict | None, name: str, source_hash: str, recipe: str,
                             directory: pathlib.Path) -> dict | None:
    descriptor = (previous or {}).get("images", {}).get(name)
    if not isinstance(descriptor, dict) or descriptor.get("_cache") != {
        "source_sha256": source_hash, "recipe": recipe
    }:
        return None
    tiles = descriptor.get("tiles")
    if not isinstance(tiles, list) or not tiles:
        return None
    for tile in tiles:
        filename = tile.get("file") if isinstance(tile, dict) else None
        if not isinstance(filename, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+", filename):
            return None
        width, height = tile.get("texture_width"), tile.get("texture_height")
        if not isinstance(width, int) or not isinstance(height, int) or width < 1 or height < 1:
            return None
        expected_size = sum((width * height) // (4 ** level) for level in range(3)) * (1 if tile.get("dxt5", False) else 4)
        target = directory / filename
        if not target.is_file() or target.stat().st_size != expected_size:
            return None
    return descriptor


def pbp_executable(data: bytes) -> bytes:
    """Return the DATA.PSP executable, rejecting malformed or truncated PBP files."""
    if len(data) < 40 or data[:4] != b"\x00PBP":
        raise ValueError("No es un EBOOT.PBP válido")
    offsets = list(struct.unpack_from("<8I", data, 8))
    if offsets[0] < 40 or offsets != sorted(offsets) or offsets[-1] > len(data):
        raise ValueError("El EBOOT.PBP tiene offsets de secciones inválidos")
    end = offsets[7]
    executable = data[offsets[6]:end]
    if not executable:
        raise ValueError("El EBOOT.PBP no contiene DATA.PSP")
    return executable


def find_matching_pbp(candidates: Iterable[pathlib.Path], prx_data: bytes) -> pathlib.Path | None:
    """Select a PBP only when its embedded DATA.PSP is byte-identical to the PRX."""
    for candidate in sorted(candidates, key=lambda path: path.stat().st_mtime, reverse=True):
        try:
            if pbp_executable(candidate.read_bytes()) == prx_data:
                return candidate
        except (OSError, ValueError):
            continue
    return None
