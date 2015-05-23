#!/usr/bin/env python
#
# Python installation script
# Update pypi package after every update:
# $ python setup.py sdist upload
#

import os
import sys

sys.path.insert(0, os.path.abspath('lib'))
from fource import __version__, __author__

try:
    from setuptools import setup, find_packages
except ImportError:
    print("Fource needs setuptools in order to build. Install it using"
            " your package manager (usually python-setuptools) or via pip (pip"
            " install setuptools).")
    sys.exit(1)

CLASSIFIERS = [
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Intended Audience :: Developers",
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Topic :: Utilities",
    "License :: OSI Approved :: MIT License",
]

# read requirements
fname = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(fname) as f:
    requires = list(map(lambda l: l.strip(), f.readlines()))


setup(name = 'fource',
      version = __version__,
      description = 'Fully automated status board application',
      author = __author__,
      author_email = 'hi@fource.in',
      url = 'http://fource.in/',
      license = 'MIT',
      install_requires = requires,
      package_dir = { '': 'lib' },
      packages = find_packages('lib'),
      classifiers = CLASSIFIERS,
      scripts = [
         'bin/fource',
      ],
      data_files = [],
)
