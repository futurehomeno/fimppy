#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

# Package meta-data.
NAME = 'fimppy'
DESCRIPTION = 'Futurehome FIMP API'
URL = 'https://github.com/futurehomeno/fimppy'
EMAIL = 'mustafa@futurehome.no'
AUTHOR = 'Mustafa Simsek'

# What packages are required for this module to be executed?
REQUIRED = [
    'paho-mqtt'
]

class install(_install):
    def run(self):
        _install.run(self)

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name=NAME,
    version='1.0.1',
    license='Proprietary',
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    py_modules=['fimppy'],
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)