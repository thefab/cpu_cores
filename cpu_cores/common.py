import sys


class CPUCoresCounter(object):

    platform = None

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
            raise NotImplemented("unsupported platform type [%s]" % cls.platform)

    def get_physical_cores_count(self):
        raise NotImplemented()

    def get_physical_processors_count(self):
        raise NotImplemented()
