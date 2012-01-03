'''
__init__.py
author: Oliver Bartley
date: 6 DEC 2011

This file is a generic drop-in to make Python-style packages of .sikuli scripts
importable. The containing dir is iterated, and each .sikuli script is
imported into the current namespace. This yields a 'dotted name' that
is consistent with standard Python, e.g:
function `spam()` in `bar.sikuli` contained in package `foo` can be accessed by
the identifier `foo.bar.spam()`
This is compatible with Pythons unittest.TestLoader functions.
'''
from org.sikuli.script import *
import os, sys, unittest

# get the absolute path to this __file__, split the filename
pkgDir = os.path.split(
        os.path.abspath(__file__)
        )[0]


if not pkgDir in sys.path:
        # add current dir to PATH
        pkgDirInPath = False
        sys.path.append(pkgDir)
else:
        # pkgDir already exists in path
        pkgDirInPath = True

# iterate through pkgDir, importing all .sikuli and adding them to CURRENT NAMESPACE
# this works around Sikuli's inability to directly import a Python-style package
for item in os.listdir(pkgDir):
    if item[-7:] == ".sikuli":
        exec ("from %s import *" % item[:-7])

# cleanup PATH if pkgDir wasn't initially present
if not pkgDirInPath: sys.path.remove(pkgDir)