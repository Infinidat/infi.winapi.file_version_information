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

This project uses buildout, and git to generate setup.py and __version__.py.
In order to generate these, run:

    python -S bootstrap.py -d -t
    bin/buildout -c buildout-version.cfg
    python setup.py develop

In our development environment, we use isolated python builds, by running the following instead of the last command:

    bin/buildout install development-scripts

