#!/usr/bin/env python
from setuptools import setup, find_packages
from firedj import __version__
 
setup(name='firedj',
    version=__version__,
    description="Django template support for Fire.app",
    classifiers=[
        "Programming Language :: Python",
        "Environment :: Web Environment",
    ],
    keywords='django,fire.app',
    author='tzangms',
    author_email='tzangms@gmail.com',
    url='http://github.com/tzangms/firedj',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django>=1.3'
    ],
    entry_points="""
    [console_scripts]
    firedj = firedj.core:main
    """
    )
