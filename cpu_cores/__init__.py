# This file is part of cpu_cores released under the MIT license.
# See the LICENSE file for more information.

version_info = (0, 1, '0')
__version__ = ".".join([str(x) for x in version_info])

from cpu_cores.common import CPUCoresCounter

__all__ = ['CPUCoresCounter']
