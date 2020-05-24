#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from pathlib import Path
from setuptools import find_packages, setup 
import pandas as pd 


ROOT_PATH = Path(__file__).parent

LICENSE_PATH = ROOT_PATH / 'LICENSE'

README_PATH = ROOT_PATH / 'README.md'

REQUIREMENTS_PATH = ROOT_PATH / 'requirements.txt'

#REQUIREMENTS_PATH = ROOT_PATH / 'requirement' / 'main.txt'

#REQUIREMENTS_TEST_PATH = ROOT_PATH / 'requirement' / 'test.txt'

#REQUIREMENTS_RQ_PATH = ROOT_PATH / 'requirement' / 'extras-rq.txt'

setup(
    name='DL_final',
    version='0.1.0',
    description='Final Project for Deep Learning',
    long_description=README_PATH.read_text(),
    long_description_content_type="text/markdown",
    author='Rafael Ortega Ramírez, Carlos Tabares Juárez Bernal, Mario Rodrí',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    license='MIT License',
)
