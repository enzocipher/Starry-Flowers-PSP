import hashlib
import json
import pathlib
import tempfile
import unittest
import zipfile

from package_psp_release import package_release


class ReleasePackageTests(unittest.TestCase):
    def fixture(self, root):
        dist = root / 'psp/dist'
        data = dist / 'DATA'
        data.mkdir(parents=True)
        (root / 'ASSETS.md').write_text('Original credits', encoding='utf-8')
        (dist / 'StarryFlowers.iso').write_bytes(b'ISO fixture')
        (dist / 'EBOOT.PBP').write_bytes(b'PBP fixture')
        files = ['MANIFEST.JSON', 'NUNITO.TXT', 'TWEMOJI.TXT', 'DEJAVU.TXT', 'RENPY.TXT', 'ART.TEX']
        for name in files[1:]:
            (data / name).write_bytes(name.encode())
        (data / 'MANIFEST.JSON').write_text(json.dumps({'files': files}), encoding='utf-8')
        return dist

    def test_package_contains_only_manifest_resources_and_checksums_match(self):
        with tempfile.TemporaryDirectory() as temporary:
            dist = self.fixture(pathlib.Path(temporary))
            for name in ['AUDIT', 'PERF', 'SAVE.JSON', 'STALE.PCM']:
                (dist / 'DATA' / name).write_text('must not ship', encoding='utf-8')
            archive, checksums = package_release(dist)
            files = json.loads((dist / 'DATA/MANIFEST.JSON').read_text())['files']
            with zipfile.ZipFile(archive) as packed:
                self.assertEqual(set(packed.namelist()), {
                    'StarryFlowers/EBOOT.PBP', 'StarryFlowers/README.txt', 'StarryFlowers/ASSETS.md',
                    *(f'StarryFlowers/DATA/{name}' for name in files),
                })
                for name in files:
                    self.assertEqual(packed.read(f'StarryFlowers/DATA/{name}'), (dist / 'DATA' / name).read_bytes())
                self.assertEqual(packed.read('StarryFlowers/EBOOT.PBP'), (dist / 'EBOOT.PBP').read_bytes())
            for line in checksums.read_text(encoding='ascii').splitlines():
                digest, name = line.split('  ')
                self.assertEqual(digest, hashlib.sha256((dist / name).read_bytes()).hexdigest())

    def test_missing_executable_license_or_audit_manifest_cannot_ship(self):
        for problem in ['missing-eboot', 'missing-license', 'AUDIT', 'PERF']:
            with self.subTest(problem=problem), tempfile.TemporaryDirectory() as temporary:
                dist = self.fixture(pathlib.Path(temporary))
                manifest_path = dist / 'DATA/MANIFEST.JSON'
                manifest = json.loads(manifest_path.read_text())
                if problem == 'missing-eboot':
                    (dist / 'EBOOT.PBP').unlink()
                elif problem == 'missing-license':
                    manifest['files'].remove('NUNITO.TXT')
                else:
                    (dist / 'DATA' / problem).touch()
                    manifest['files'].append(problem)
                manifest_path.write_text(json.dumps(manifest), encoding='utf-8')
                with self.assertRaises((FileNotFoundError, ValueError)):
                    package_release(dist)
                self.assertFalse((dist / 'StarryFlowers-homebrew.zip').exists())


if __name__ == '__main__':
    unittest.main()
