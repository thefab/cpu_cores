version_info = (0, 1, '0')
__version__ = ".".join([str(x) for x in version_info])

from cpu_cores.common import CPUCoresCounter

__all__ = ['CPUCoresCounter']
