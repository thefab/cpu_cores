#!/usr/bin/env python

# This file is part of cpu_cores released under the MIT license.
# See the LICENSE file for more information.

import argparse
import sys

from cpu_cores import CPUCoresCounter

description = 'Get the number of real physical cpu cores and processors'
parser = argparse.ArgumentParser(description=description)
parser.parse_args()

try:
    c = CPUCoresCounter.factory()
    procs_count = c.get_physical_processors_count()
    cores_count = c.get_physical_cores_count()
except:
    sys.stderr.write("Can't read the number of processors/cores"
                     "(platform=%s)\n" % c.platform)
    sys.exit(1)

print("Number of real physical processors : %i" % procs_count)
print("Number of real physical cores      : %i" % cores_count)
