cpu\_cores
==========

What is it ?
------------

``cpu_cores`` is small python library and utility to get the number of
"physical" cpu cores (without hyperthreading logical cores) of a
linux/osx box.

On Linux, this is not an easy task because of hyperthreaded logical
cores included in ``/proc/cpuinfo``. Please, read carefully `this
excellent post <http://www.richweb.com/cpu_info>`_ to understand why.

Special features
----------------

-  support Linux (well tested) and OSX (needs some extra tests files),
   easy to extend to support other OS
-  unit tests (> 90% coverage)
-  python2 and python3 support
-  no dependencies

Usage
~~~~~

See the `README <https://github.com/thefab/cpu_cores/blob/master/README.md>`_ for more details.
