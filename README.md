# cpu_cores

## Status (master branch)

[![Build Status](https://travis-ci.org/thefab/cpu_cores.png)](https://travis-ci.org/thefab/cpu_cores)

## What is it ?

`cpu_cores` is small python library and utility to get the number of "physical" cpu cores (without hyperthreading logical cores) of a linux/osx box.

On Linux, this is not an easy task because of hyperthreaded logical cores included in `/proc/cpuinfo`. Please, read carefully [this excellent post](http://www.richweb.com/cpu_info) to understand why.

## Special features

- support Linux (well tested) and OSX (needs some extra tests files), easy to extend to support other OS
- unit tests (> 90% coverage)
- python2 and python3 support
- no dependencies

## Warning

`cpu_cores` is at an early stage of development (API can change).

If you have exotic Linux or OSX boxes with plenty of cpu cores, please provides the output of :

    # For Linux
    cat /proc/cpuinfo

    or

    # For OSX
    /usr/sbin/system_profiler -detailLevel full SPHardwareDataType

## Quickstart

### Installation

    pip install cpu_cores

    Requirements: 
    - Python 2.6, 2.7, 3.2 or 3.3

## Two ways to use it

### As a python library

    #!/usr/bin/env python

    # Import
    from cpu_cores import CPUCoresCounter

    # We build an instance for the current operating system
    instance = CPUCoresCounter.factory()

    # Get the number of total real cpu cores
    print instance.get_physical_cores_count()

    # Get the number of total physical processors
    print instance.get_physical_processors_count()

### As a CLI utility

    prompt$ get_cpu_physical_cores.py
    Number of real physical processors : 1
    Number of real physical cores      : 2


    prompt$ get_cpu_physical_cores.py --single-value=cores
    2


    prompt$ get_cpu_physical_cores.py --single-value=processors
    1

