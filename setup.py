#!/usr/bin/env python2

import os, codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

def read(filename):
    """
    Get the long description from a file.
    """
    fname = os.path.join(here, filename)
    with codecs.open(fname, encoding='utf-8') as f:
        return f.read()

setup(
    name='checkpoint',
    version='0.0.1',
    description='RFID reader control library',
    long_description=read('README.md'),
    author='RodriguesFAS',
    author_email='francsicosouzaacer@gmail.com',
    url='#',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='checkpoint llrp rfid reader',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
