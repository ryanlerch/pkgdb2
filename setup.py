#!/usr/bin/env python

"""
Setup script
"""

# Required to build on EL6
__requires__ = ['SQLAlchemy >= 0.7', 'jinja2 >= 2.4']
import pkg_resources

from setuptools import setup
from pkgdb import __version__

def get_requires():
    ''' Reads the requirements.txt and return its content in a list. '''
    stream = open('requirements.txt')
    content = stream.readlines()
    stream.close()

    deps = []
    for row in content:
        if row.startswith('#'):
            continue
        else:
            deps.append(row.strip())

    return deps


requires = get_requires()

setup(
    name='packagedb',
    description='PackageDB is the Package database for Fedora.',
    version=__version__,
    author='Pierre-Yves Chibon',
    author_email='pingou@pingoured.fr',
    maintainer='Pierre-Yves Chibon',
    maintainer_email='pingou@pingoured.fr',
    license='GPLv3+',
    download_url='https://fedorahosted.org/releases/p/a/packagedb/',
    url='https://fedorahosted.org/packagedb/',
    packages=['pkgdb'],
    include_package_data=True,
    install_requires=requires
    )
