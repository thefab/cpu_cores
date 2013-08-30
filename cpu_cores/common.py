import sys


class CPUCoresCounter(object):

    platform = None
    _physical_cores_count = None
    _physical_processors_count = None

    def _count(self, *args, **kwargs):
        raise NotImplementedError()

    @classmethod
    def factory(cls, force_platform=None):
        if force_platform is not None:
            cls.platform = force_platform
        else:
            cls.platform = sys.platform
        if cls.platform == 'darwin':
            from cpu_cores.darwin import DarwinCPUCoresCounter
            return DarwinCPUCoresCounter()
        elif cls.platform == 'linux':
            from cpu_cores.linux import LinuxCPUCoresCounter
            return LinuxCPUCoresCounter()
        else:
            raise NotImplementedError("unsupported platform type [%s]" % cls.platform)

    def get_physical_processors_count(self):
        self._check_counting_or_do_it()
        return self._physical_processors_count

    def get_physical_cores_count(self):
        self._check_counting_or_do_it()
        return self._physical_cores_count
