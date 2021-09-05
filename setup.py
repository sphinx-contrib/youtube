# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the youtube Sphinx extension.

The extension defines the directives, "youtube" and "vimeo", for embedding 
YouTube and Vimeo videos, respectively. 
'''

requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-youtube',
    version='1.0.0',
    url='https://github.com/sphinx-contrib/youtube',
    license='BSD',
    author='Chris Pickel',
    author_email='sfiera@gmail.com',
    maintainer='David A. Ham',
    maintainer_email='david.ham@imperial.ac.uk',
    description='Sphinx "youtube" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
