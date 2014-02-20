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

This project uses buildout and infi-projector, and git to generate setup.py and __version__.py.
In order to generate these, first get infi-projector:

    easy_install infi.projector

    and then run in the project directory:

        projector devenv build
