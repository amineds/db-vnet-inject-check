#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='Distutils',
      version='0.1',
      description='Check network configuration for a VNET-injected workspace',
      author='Databricks',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=[
	     'azure',
      	'requests',
      	'databricks-cli'
      ],
)
