# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import setup, find_packages


setup(name='lwb',
      version='1.0',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      entry_points={
          'console_scripts': [
              'lwb = lwb.main:__main__',
          ],
      },
      )
