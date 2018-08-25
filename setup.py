from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']

setup(
    name='Mopidy-MediaButton',
    version=get_version('mopidy_mediabutton/__init__.py'),
    url='https://github.com/BookSwapSteve/Mopidy_MediaButton',
    license='Apache License, Version 2.0',
    author='Stephen Harrison',
    author_email='Stephen.Harrison@AnalysisUK.com',
    description='Mopidy extension allowing for play/pause and volume control with a BlueTooth media button',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
        'requests >= 2.0',
        'cachetools >= 1.0',
    ],
    entry_points={
        'mopidy.ext': [
            'mediabutton = mopidy_mediabutton:MediaButtonExtension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
