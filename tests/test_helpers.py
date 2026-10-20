"""Portable checks: python -B -m unittest discover -s tests -v"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SKILL = Path(__file__).resolve().parents[1]
INVENTORY = SKILL / 'scripts' / 'project_inventory.py'


class HelperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='wolf-skill-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = self.root / 'game with spaces and 日本語'
        self.basic = self.project / 'Data' / 'BasicData'
        self.basic.mkdir(parents=True)
        (self.basic / 'Game.dat').write_bytes(b'opaque\x00data')
        (self.project / 'Editor.exe').write_bytes(b'fixture only; never executed')

    def invoke(self, *args, code=0):
        run = subprocess.run([sys.executable, '-B', str(INVENTORY), *map(str, args)],
                             capture_output=True, encoding='utf-8')
        self.assertEqual(run.returncode, code, run.stdout + run.stderr)
        return json.loads(run.stdout)

    def manifest(self, name, hashed=True, encoding='utf-8'):
        report = self.invoke('scan', self.project, *(['--hash'] if hashed else []))
        path = self.root / name
        path.write_text(json.dumps(report), encoding=encoding)
        return path

    def test_scan_preserves_bytes(self):
        digest = lambda: hashlib.sha256((self.basic / 'Game.dat').read_bytes()).hexdigest()
        before = digest()
        report = self.invoke('scan', self.project, '--hash')
        self.assertTrue(report['complete'])
        self.assertTrue(report['markers']['Editor.exe'])
        self.assertEqual(before, digest())
        self.assertEqual(len(report['files']), 2)

    def test_detects_all_byte_changes_and_supports_powershell_reports(self):
        before = self.manifest('before.json', encoding='utf-16')
        (self.basic / 'Game.dat').write_bytes(b'OPAQUE\x00data')
        (self.basic / 'Added.dat').write_bytes(b'new')
        (self.project / 'Editor.exe').unlink()
        after = self.manifest('after.json', encoding='utf-8-sig')
        report = self.invoke('diff', before, after, code=1)
        self.assertEqual({item['kind'] for item in report['changes']}, {'added', 'removed', 'modified'})
        self.assertEqual(report['unexpected_count'], 3)
        report = self.invoke('diff', before, after, '--allow', 'Data/*', '--allow', 'Editor.exe')
        self.assertEqual(report['unexpected_count'], 0)
        self.assertEqual(len(report['changes']), 3)

    def test_rejects_incomplete_input_and_layout_escape(self):
        unhash = self.manifest('unhashed.json', hashed=False)
        hashed = self.manifest('hashed.json')
        self.invoke('diff', unhash, hashed, code=2)
        bad = self.root / 'bad.json'
        bad.write_text('[]', encoding='utf-8')
        self.invoke('diff', bad, hashed, code=2)
        self.invoke('scan', self.project, '--data-dir', '../escape', code=2)

    def test_lookup_after_relocation_without_dependencies(self):
        copy = self.root / 'relocated skill'
        shutil.copytree(SKILL, copy, ignore=shutil.ignore_patterns('__pycache__'))
        run = subprocess.run([sys.executable, '-B', str(copy / 'scripts' / 'lookup.py'), 'Sys143'],
                             capture_output=True, encoding='utf-8')
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn('Pro Commands Available', run.stdout)
        self.assertNotIn('Sys141', run.stdout)
        empty = subprocess.run([sys.executable, '-B', str(copy / 'scripts' / 'lookup.py'), 'unknown-no-such-topic'],
                               capture_output=True, encoding='utf-8')
        self.assertEqual(empty.returncode, 1)


if __name__ == '__main__':
    unittest.main()
