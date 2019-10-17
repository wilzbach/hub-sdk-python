#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import subprocess
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

VERSION = '0.1.9'
DESCRIPTION = 'A Python SDK to access the Storyscript Hub, ' \
              'which supports caching and more'


root_dir = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(root_dir, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(root_dir, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        subprocess.run(
            [sys.executable, 'setup.py', 'sdist', 'bdist_wheel',
             '--universal'],
            check=True)

        self.status('Uploading the package to PyPI via Twine…')
        subprocess.run(['twine', 'upload', 'dist/*'], check=True, shell=True)

        sys.exit()


setup(
    name='story-hub',
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Storyscript',
    author_email='support@storyscript.io',
    url='https://github.com/storyscript/hub-sdk-python',
    packages=find_packages(exclude=('build.*', 'tests', 'tests.*')),
    python_requires='>=3.6',
    install_requires=[
        'requests~=2.21',
        'peewee~=3.9',
        'cachetools~=3.1',
        'appdirs~=1.4',
    ],
    tests_require=[
        'pytest==4.3.1',
        'pytest-mock==1.10.2',
        'pytest-cov==2.6.1'
    ],
    use_scm_version=True,
    setup_requires=[
        'pytest-runner==4.4',
        'setuptools_scm~=3.3',
    ],
    cmdclass={'upload': UploadCommand},
)
