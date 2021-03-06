#!/usr/bin/env python

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(name='epNamer',
      version='0.11.5',
      description='Names TV episode files in a folder based the filename and user input.',
      author='Bevan Philip',
      author_email='arrivance@gmail.com',
      url='http://github.com/arrivance/ep_namer',
      packages=['epNamerLib'],
      license='MIT',

	  classifiers=[
	    'Development Status :: 4 - Beta',

	    # Indicate who your project is intended for
	    'Intended Audience :: television viewers',
	    'Topic :: File naming',

	    # Pick your license as you wish (should match "license" above)
	    'License :: OSI Approved :: MIT License',

	    'Programming Language :: Python :: 3',
	    'Programming Language :: Python :: 3.2',
	    'Programming Language :: Python :: 3.3',
	    'Programming Language :: Python :: 3.4',
    ],

      keywords='tv, episode namer, ep_namer, tvnamer, epnamer',

      install_requires=['tvdb_api', 'hachoir3-superdesk'],

      scripts=['epNamer.py']
     )

