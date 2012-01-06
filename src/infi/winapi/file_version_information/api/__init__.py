
from infi import instruct, crap
import ctypes
import os
from ctypes import c_wchar_p as LPWSTR
from ctypes import c_wchar_p as LPCWSTR
from ctypes import c_ulong as BOOL
from ctypes import c_ulong as DWORD

class VS_FIXEDFILEINFO(instruct.Struct):
    _fields_ = [instruct.ULInt32("dwSignature"),
                instruct.ULInt32("dwStrucVersion"),
                instruct.ULInt32("dwFileVersionMS"),
                instruct.ULInt32("dwFileVersionLS"),
                instruct.ULInt32("dwProductVersionMS"),
                instruct.ULInt32("dwProductVersionLS"),
                instruct.ULInt32("dwFileFlagsMask"),
                instruct.ULInt32("dwFileFlags"),
                instruct.ULInt32("dwFileOS"),
                instruct.ULInt32("dwFileType"),
                instruct.ULInt32("dwFileSubtype"),
                instruct.ULInt32("dwFileDateMS"),
                instruct.ULInt32("dwFileDateLS"),
                ]

class GetFileVersionInfoW(crap.WrappedFunction):
    return_value = ctypes.c_byte

    @classmethod
    def get_errcheck(cls):
        return crap.errcheck_zero()

    @classmethod
    def get_library_name(cls):
        return "version.dll"

    @classmethod
    def get_parameters(cls):
        return ((ctypes.c_wchar_p, crap.IN, "strFileName"),
                (ctypes.c_ulong, 0, "handle"),
                (ctypes.c_ulong, crap.IN, "len"),
                (ctypes.c_void_p, crap.IN_OUT, "data"),)

def errcheck_zero():
    """ this error checker raises a RuntimeError if the returned value is zero
    """
    def errcheck(result, func, args):
        if result == 0:
            raise RuntimeError(result)
        return result
    return errcheck

class GetFileVersionInfoSizeW(crap.WrappedFunction):
    return_value = ctypes.c_ulong

    @classmethod
    def get_errcheck(cls):
        return errcheck_zero()

    @classmethod
    def get_library_name(cls):
        return "version.dll"

    @classmethod
    def get_parameters(cls):
        return ((ctypes.c_wchar_p, crap.IN, "strFileName"),
                (ctypes.c_void_p, crap.IN_OUT, "dwHandle", 0),)

class VerQueryValueW(crap.WrappedFunction):
    return_value = ctypes.c_byte

    @classmethod
    def get_errcheck(cls):
        return crap.errcheck_zero()

    @classmethod
    def get_library_name(cls):
        return "version.dll"

    @classmethod
    def get_parameters(cls):
        return ((ctypes.c_void_p, crap.IN, "block"),
                (ctypes.c_void_p, crap.IN, "subBlock"),
                (ctypes.POINTER(ctypes.c_void_p), crap.IN_OUT, "buffer"),
                (ctypes.POINTER(ctypes.c_ulong), crap.IN_OUT, "len"),)

def HIWORD(number):
    return (number & 0xFFFF0000) >> 16

def LOWORD(number):
    return number & 0xFFFF

