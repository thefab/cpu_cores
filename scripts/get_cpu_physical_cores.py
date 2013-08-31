#!/usr/bin/env python

# This file is part of cpu_cores released under the MIT license.
# See the LICENSE file for more information.

import argparse
import sys

from cpu_cores import CPUCoresCounter

description = 'Get the number of real physical cpu cores and processors'
parser = argparse.ArgumentParser(description=description)
parser.add_argument("-s", "--single-value", type=str, default=None,
                    dest="single_value",
                    help="just display a single value "
                         "(use 'cores' or 'processors')")
args = parser.parse_args()

single_value = None
if args.single_value:
    if args.single_value not in ('cores', 'processors'):
        stderr = sys.stderr
        stderr.write("ERROR : single_value must be 'cores' or 'processors'\n")
        parser.print_help()
    single_value = args.single_value

try:
    c = CPUCoresCounter.factory()
    procs_count = c.get_physical_processors_count()
    cores_count = c.get_physical_cores_count()
except:
    sys.stderr.write("Can't read the number of processors/cores"
                     "(platform=%s)\n" % c.platform)
    sys.exit(1)

if single_value == "cores":
    print(cores_count)
elif single_value == "processors":
    print(procs_count)
else:
    print("Number of real physical processors : %i" % procs_count)
    print("Number of real physical cores      : %i" % cores_count)
