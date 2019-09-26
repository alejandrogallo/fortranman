#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import glob


def get_version(filename):
    """Extract the package version"""
    with open(filename) as in_fh:
        for line in in_fh:
            if line.startswith('__version__'):
                return line.split('=')[1].strip()[1:-1]
    raise ValueError("Cannot extract version from %s" % filename)


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = []

dev_requirements = [
    'coverage', 'pytest', 'pytest-cov', 'pytest-xdist', 'twine', 'pep8',
    'flake8', 'wheel', 'sphinx', 'sphinx-autobuild', 'sphinx_rtd_theme']

version = get_version('./src/fortranman/__init__.py')

setup(
    author="Alejandro Gallo",
    author_email='aamsgallo@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Man pages for fortran",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            'fortranman=fortranman:main',
        ],
    },
    extras_require={
        'dev': dev_requirements,
    },
    data_files=[
        ("./fortranman/", glob.glob("manpages/man-pages-fortran/**/*.3f")),
        ("./fortranman/", glob.glob("manpages/lapack-manpages/man/man3/*")),
    ],
    license="GNU General Public License v3",
    long_description=readme,
    include_package_data=True,
    keywords='fortranman',
    name='fortranman',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/alejandrogallo/fortranman',
    version=version,
    zip_safe=False,
)
