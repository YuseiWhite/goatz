#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    name='tennis_count_app',
    version='0.0.1',
    packages=['game_app', 'game_app.models', 'game_app.controller', 'game_app.views'],
    # You could use find_packages if setuptools is installed.
    # packages=find_packages(),
    package_data={'game_app': ['templates/*.txt']},
    url='https://www.tennis_count_app.com',
    license='MIT',
    author='yusir',
    author_email='example@example.com',
    # You can specify install_requires if setuptools is installed
    # install_requires=['termcolor==1.1.0'],
    long_description=open('README.txt').read(),
)
