# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import setup, find_packages


setup(name='lnb',
      version='1.0',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      entry_points={
          'console_scripts': [
              'lnb = lnb.main:__main__',
          ],
      },
      )
