#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-07-29 13:51:11
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-07-29 13:52:05

from setuptools import setup, find_packages

## Get our requirements from our .txt file
with open('requirements.txt') as requirements:
	modules = [line.strip('\n') for line in requirements]

setup(name = 'acme_wines',
	version = '0.1',
	description = 'A backend RESTful service for wine order managemment',
	author = 'Vinoth Kumar',
	install_requires = modules
)