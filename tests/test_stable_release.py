import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('promote', ROOT / 'scripts/promote_stable.py')
promote = importlib.util.module_from_spec(spec)
spec.loader.exec_module(promote)

class StableReleaseTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'releases/stable.json').read_text())

    def test_official_request(self):
        self.assertEqual(promote.validate_request(self.data)[0], 'v' + self.data['versionName'])

    def test_external_asset_is_rejected(self):
        self.data['apkUrl'] = 'https://example.com/app.apk'
        with self.assertRaises(ValueError): promote.validate_request(self.data)

    def test_invalid_version_and_hash_are_rejected(self):
        for field, value in [('versionName', '../main'), ('versionCode', True), ('sha256', 'bad')]:
            data = copy.deepcopy(self.data)
            data[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): promote.validate_request(data)

    def test_downgrade_is_rejected(self):
        current = dict(self.data, versionCode=self.data['versionCode'] + 1)
        with self.assertRaises(ValueError): promote.validate_upgrade(current, self.data)

    def test_same_version_cannot_replace_binary(self):
        current = dict(self.data, sha256='0' * 64)
        with self.assertRaises(ValueError): promote.validate_upgrade(current, self.data)

    def test_identical_retry_and_newer_version_are_allowed(self):
        promote.validate_upgrade(self.data, self.data)
        promote.validate_upgrade(dict(self.data, versionCode=self.data['versionCode'] - 1), self.data)
