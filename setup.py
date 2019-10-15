#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

readme_contents = 'A Python SDK to access the Storyscript Hub, '
'which supports caching and more'

setup(
    name='story-hub',
    version='0.1.8',
    description='A Python SDK to access the Storyscript Hub, '
                'which supports caching and more',
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='Storyscript',
    author_email='support@storyscript.io',
    url='https://github.com/storyscript/hub-sdk-python',
    packages=find_packages(exclude=('build.*', 'tests', 'tests.*')),
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
    setup_requires=['pytest-runner==4.4']
)
