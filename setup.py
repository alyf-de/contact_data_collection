# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in contact_data_collection/__init__.py
from contact_data_collection import __version__ as version

setup(
	name='contact_data_collection',
	version=version,
	description='Contact Data Collection for compliance with COVID-19 related regulations.',
	author='ALYF GmbH',
	author_email='hallo@alyf.de',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
