from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "pypitchfx: A tool for downloading, analyzing, and visualizing pitchfx data"
# Long description will go up on the pypi page
long_description = """

pypitchfx
========
pypitchfx is a tool for downloading, analyzing, and visualizing pitchfx data.

It contains a parser for obtaining the pitch data from MLB. The pitch data is
written out to a csv file that is easy to be parsed with most statistical software.
The analysis portion of the code is written using pandas dataframes to easily
make selections and manipulate data. Finally, visualizations are implemented with
matplotlib.

License
=======
``pypitchfx`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

Copyright (c) 2017-- Greg Lucas
"""

NAME = "pypitchfx"
MAINTAINER = "Greg Lucas"
MAINTAINER_EMAIL = "greg.m.lucas@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/greglucas/pypitchfx"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Greg Lucas"
AUTHOR_EMAIL = "greg.m.lucas@gmail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'pypitchfx': [pjoin('data', '*')]}
REQUIRES = ["lxml,pandas,matplotlib,numpy"]
