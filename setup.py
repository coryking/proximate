#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    author = 'George V. Reilly <GeorgeR@cozi.com>',
    name = 'Proximate',
    version = '0.1.1',
    packages = find_packages(),
    package_data ={},
    install_requires = [
        'Paste',
        'WSGIProxy',
    ],
    description = 'None',
    entry_points = {
        'console_scripts': [
            'proximate = proximate.proxy:proximate',
            ]
    },
)
