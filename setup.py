#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='mnt',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Mount encrypted filesystems.",
    long_description="Mount and manage encrypted filesystems.",
    scripts=['mnt'],
    data_files=[('share/man/man1', ['mnt.1'])],
)
