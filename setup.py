#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name='napari-terrible',
    version='0.0.1',
    author='Malicious User',
    author_email='mean_guy@his.computer.com',
    license='BSD-3',
    url='https://github.com/tlambert03/terrible',
    description="Don't ever use this plugin",
    py_modules=['napari_terrible'],
    python_requires='>=3.6',
    install_requires=['napari_plugin_engine'],
    entry_points={
        'napari.plugin': [
            'terrible = napari_terrible',
        ],
    },
)
