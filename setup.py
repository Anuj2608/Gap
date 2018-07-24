#!/usr/bin/env python

from setuptools import setup, find_packages
import os, sys

install_requires=[
  'numpy',
  'h5py',
  'unidecode',
  'nltk',
  'opencv-python']
		  
tests_require=[
  'pytest',
  'pytest-cov']
		  
scripts=[
  'scripts/address.py',
  'scripts/pdf_res.py',
  'scripts/perf.py',
  'scripts/segment.py',
  'scripts/splitter.py',
  'scripts/syntax.py',
  'scripts/vision.py',
  'scripts/vocabulary.py']

setup(
  name='Gap-ML',
  version='0.9',
  description='NLP and CV Data Engineering Framework',
  author='Andrew Ferlitsch',
  author_email='aferlitsch@gmail.com',
  license='CC-BY',
  url='https://github.com/andrewferlitsch/Gap',
  packages=find_packages(),
  install_requires=install_requires,
  tests_require=tests_require,
  scripts=scripts
)

if sys.platform.startswith('win'):
    pass
elif sys.platform.startswith('linux'):
    #install Ghostscript:
    os.system('sudo apt-get update && sudo apt-get install ghostscript')
    #install ImageMagick:
    os.system('sudo apt-get install imagemagick')
    #install Tesseract:
    os.system('sudo apt-get install tesseract-ocr && sudo apt-get install tesseract-ocr-eng')
elif sys.platform.startswith('darwin'):
    os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    os.system('brew update')
    os.system('brew install ghostscript imagemagick tesseract')
