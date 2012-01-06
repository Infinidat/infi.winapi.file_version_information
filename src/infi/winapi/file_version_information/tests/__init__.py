
import mock
import os
import ctypes
from infi import unittest
from .. import  File, api
from pkg_resources import parse_version
from contextlib import nested, contextmanager

CMD_EXE_PATH = r"C:\Windows\System32\cmd.exe"

class FileTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(FileTestCase, cls).setUpClass()
        if os.name != 'nt':
            raise unittest.SkipTest("This test can run only on Windows")

    def test_version_of_cmd_exe(self):
        cmd_exe = File(CMD_EXE_PATH)
        version = cmd_exe.get_version()
        self.assertGreater(parse_version(version), parse_version('1.0'))

class MockFileTestCase(FileTestCase):
    @classmethod
    def setUpClass(cls):
        with mock.patch.object(os, "name", new='nt'):
            super(MockFileTestCase, cls).setUpClass()

    def _patch_exists(self, path):
        self.assertEqual(path, CMD_EXE_PATH)
        return True

    def _patch_GetFileVersionInfoSizeW(self, filepath):
        self.assertEqual(filepath.value, CMD_EXE_PATH)
        return 1828

    def test_version_of_cmd_exe(self):
        with nested(mock.patch.object(os.path, "exists", self._patch_exists),
                    mock.patch.object(api, "GetFileVersionInfoSizeW", self._patch_GetFileVersionInfoSizeW),):
            super(MockFileTestCase, self).test_version_of_cmd_exe()

