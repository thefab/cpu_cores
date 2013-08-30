#!/usr/bin/env python
#
# This file is part of cpu_cores released under the MIT license.
# See the LICENSE file for more information.

from setuptools import setup, find_packages
import cpu_cores

DESCRIPTION = "cpu_cores-py is a small python library to get the number of" +\
              "'real physical' cpu cores of a linux/osx box"
try:
    with open('PIP.rst') as f:
        LONG_DESCRIPTION = f.read()
except IOError:
    LONG_DESCRIPTION = DESCRIPTION

with open('pip-requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not
                                                     line.startswith('--'))]

setup(
    name='cpu_cores',
    version=cpu_cores.__version__,
    author="Fabien MARTY",
    author_email="fabien.marty@gmail.com",
    url="https://github.com/thefab/cpu_cores",
    packages=find_packages(),
    license='MIT',
    download_url='https://github.com/thefab/cpu_cores',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    scripts=["scripts/get_cpu_physical_cores.py"],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities',
        'Topic :: System :: Hardware',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development',
    ]
)
