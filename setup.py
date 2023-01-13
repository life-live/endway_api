#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codecs import open
from os import path

from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

version = "1.1"

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="endway_api",
    version=version,
    description="Library for convenient work with the EndWay forum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/life-live/endway_api",
    author="life-live",
    author_email="I-will-tell-you@everything.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=["endway_api"],
    include_package_data=True,
    install_requires=["requests", "bs4"]
)
