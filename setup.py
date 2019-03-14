#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ソースコードディストリビューションsetupです。
$ python setup.py sdist
"""

__author__ = 'Nobuyasu Koretsu'
__version__ = '1.0.0'
__date__ = '2019/03/14'

from distutils.core import setup

setup( \
	name='Todo', \
	version=__version__, \
	description='Todo written by Python', \
	author=__author__, \
	author_email='einsatzkommandocobra.1996@gmail.com', \
	license='(null)', \
	long_description='ターミナル上で動く使いにくいTodoリストを作成します', \
	platforms='macOS (10.14.2) Mojave', \
	packages=['todo'], \
)