Overview
========

Simple API to retreive a Windows file version

Usage
-----

Here's an example on how to use this module:

    >>> from infi.winapi.file_version_information import File
    >>> f = File(r"C:\Windows\System32\cmd.exe")
    >>> f.get_file_version()
    "6.1.7601.17514"

Checking out the code
=====================

Run the following:

    easy_install -U infi.projector
    projector devenv build

Python 3 support is experimental and not fully tested.
