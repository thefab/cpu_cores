import shlex
import subprocess

from cpu_cores.common import CPUCoresCounter

CPUINFO_COMMAND = "/usr/sbin/system_profiler -detailLevel full SPHardwareDataType"


class DarwinCPUCoresCounter(CPUCoresCounter):

    def _count(self, command):
        s = subprocess.Popen(shlex.split(command),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        if s:
            out, err = s.communicate()
            if len(err.strip()) > 0 or len(out.strip()) == 0:
                raise Exception('impossible to get the cpu cores count (darwin)' + \
                                ' (error message = %s)' % err.strip())
            lines = out.split('\n')
            for line in lines:
                tmp = line.strip()
                if tmp.startswith('Total Number of Cores:'):
                    self._physical_cores_count = int(tmp.split(':')[1])
                if tmp.startswith('Number of Processors:'):
                    self._physical_processors_count = int(tmp.split(':')[1])
        if self._physical_processors_count is None or \
                self._physical_cores_count is None:
            raise Exception('impossible to get the cpu cores count (darwin)')

    def _check_counting_or_do_it(self):
        if self._physical_processors_count is None or \
                self._physical_cores_count is None:
            self._count(CPUINFO_COMMAND)
