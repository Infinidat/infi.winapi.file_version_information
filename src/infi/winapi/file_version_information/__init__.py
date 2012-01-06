__import__("pkg_resources").declare_namespace(__name__)

import ctypes
import os
from . import api

class File(object):
    def __init__(self, filepath):
        super(File, self).__init__()
        self._path = filepath

    def _get_version_info_size(self):
        filepath = ctypes.create_unicode_buffer(self._path)
        size = api.GetFileVersionInfoSizeW(filepath)
        return size

    def _extract_version_info_from_block(self, block):
        sub_block = ctypes.create_unicode_buffer(u"\\")
        size = ctypes.c_ulong(api.VS_FIXEDFILEINFO.min_max_sizeof().max)
        pointer = ctypes.c_void_p()
        api.VerQueryValueW(block, sub_block, pointer, size)
        buffer = ctypes.string_at(pointer, size.value)
        return api.VS_FIXEDFILEINFO.create_from_string(buffer)

    def _get_version_info(self):
        size = ctypes.c_ulong(self._get_version_info_size())
        block = ctypes.c_buffer('\x00' * size.value, size.value)
        filepath = ctypes.create_unicode_buffer(self._path)
        api.GetFileVersionInfoW(filepath, ctypes.c_ulong(0), size, block)
        return block

    def get_version(self):
        assert os.path.exists(self._path)
        block = self._get_version_info()
        info = self._extract_version_info_from_block(block)
        items = [api.HIWORD(info.dwFileVersionMS), api.LOWORD(info.dwFileVersionMS),
                api.HIWORD(info.dwFileVersionLS), api.LOWORD(info.dwFileVersionLS)]
        return ".".join([str(item) for item in items])

