# encoding: utf8

from setuptools import find_packages
from setuptools import setup

setup(
  zip_safe=True,
  name='zae',
  version='0.0.1',
  description='zae tools',
  long_description='zae tools',
  url='https://github.com/anthonyrisinger/zae',
  author='C Anthony Risinger',
  author_email='c@anthonyrisinger.com',
  license='BSD',
  classifiers=[
    'License :: Other/Proprietary License',
    'Development Status :: 2 - Pre-Alpha',
    'Programming Language :: Python',
    ],
  packages=find_packages(include=['zae', 'zae.*']),
  entry_points={
    'console_scripts': [
      'zae = zae:main',
      ],
    },
  install_requires=[
     'click < 6.8',
    ],
  )
