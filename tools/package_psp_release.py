from __future__ import annotations

import json
import zipfile
from pathlib import Path

import psp_pipeline


def package_release(dist: Path) -> tuple[Path, Path]:
    data = dist / "DATA"
    manifest_path = data / "MANIFEST.JSON"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    psp_pipeline.validate_manifest(manifest, data)

    iso = dist / "StarryFlowers.iso"
    eboot = dist / "EBOOT.PBP"
    for path in (iso, eboot):
        if not path.is_file() or path.stat().st_size == 0:
            raise FileNotFoundError(f"Missing or empty required release file: {path}")

    files = manifest.get("files", [])
    required = {"NUNITO.TXT", "TWEMOJI.TXT", "DEJAVU.TXT", "RENPY.TXT"}
    names = {Path(name).name.upper() for name in files}
    missing = sorted(required - names)
    if missing:
        raise ValueError(f"Manifest is missing license files: {', '.join(missing)}")

    for name in files:
        filename = Path(name).name.upper()
        if filename.startswith(("AUDIT", "PERF")):
            raise ValueError(f"Manifest must not include audit or performance file: {name}")

    assets = dist.parents[1] / "ASSETS.md"
    if not assets.is_file():
        raise FileNotFoundError(f"Missing repository asset documentation: {assets}")

    archive = dist / "StarryFlowers-homebrew.zip"
    with zipfile.ZipFile(
        archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6
    ) as zf:
        zf.write(eboot, "StarryFlowers/EBOOT.PBP")
        for name in sorted(files):
            zf.write(data / name, f"StarryFlowers/DATA/{name}")
        zf.write(assets, "StarryFlowers/ASSETS.md")
        zf.writestr(
            "StarryFlowers/README.txt",
            "Install:\n"
            "1. Copy the StarryFlowers folder to PSP/GAME/ on your Memory Stick.\n"
            "Save data is stored in PSP/SAVEDATA/STARRYFLOWERS.\n",
        )

    checksums = dist / "SHA256SUMS.txt"
    checksums.write_text(
        f"{psp_pipeline.sha256_file(iso)}  {iso.name}\n"
        f"{psp_pipeline.sha256_file(archive)}  {archive.name}\n",
        encoding="ascii",
        newline="\n",
    )
    return archive, checksums


def main() -> None:
    archive, checksums = package_release(
        Path(__file__).resolve().parents[1] / "psp/dist"
    )
    print(archive)
    print(checksums)


if __name__ == "__main__":
    main()
