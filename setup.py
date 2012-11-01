#!/usr/bin/env python

from distutils.core import setup
from ecto.package import parse_package_for_distutils

d = parse_package_for_distutils()
d['packages'] = ['object_recognition_tod']
d['package_dir'] = {'': 'python'}
d['install_requires'] = []

setup(**d)
