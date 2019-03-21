#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'fimppy'
DESCRIPTION = 'Futurehome FIMP API'
URL = 'https://github.com/futurehomeno/fimppy'
EMAIL = 'mustafa@futurehome.no'
AUTHOR = 'Mustafa Simsek'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = 1.0

# What packages are required for this module to be executed?
REQUIRED = [
    'paho-mqtt'
]

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=NAME,
    version='0.0.1',
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)