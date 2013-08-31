# This file is part of cpu_cores released under the MIT license.
# See the LICENSE file for more information.

import unittest
import os

from cpu_cores import CPUCoresCounter


class TestLinux(unittest.TestCase):

    def _dir(self):
        return os.path.dirname(__file__)

    def test_factory_linux(self):
        x = CPUCoresCounter.factory(force_platform='linux')
        self.assertTrue(x is not None)
        self.assertTrue(x.platform is not None)
        self.assertTrue(x.platform == 'linux')

    def _test_linux_count(self, file_name, processors_count, cores_count):
        x = CPUCoresCounter.factory(force_platform='linux')
        self.assertTrue(x is not None)
        self.assertTrue(x.platform is not None)
        self.assertTrue(x.platform == 'linux')
        x._count(os.path.join(self._dir(), file_name))
        self.assertEqual(x._physical_processors_count, processors_count)
        self.assertEqual(x._physical_cores_count, cores_count)
        return x

    def test_linux_count1(self):
        self._test_linux_count('linux1', 2, 4)

    def test_linux_count2(self):
        self._test_linux_count('linux2', 1, 1)

    def test_linux_count3(self):
        self._test_linux_count('linux3', 2, 8)

    def test_linux_count4(self):
        self._test_linux_count('linux4', 1, 1)

    def test_linux_count5(self):
        self._test_linux_count('linux5', 1, 1)

    def test_linux_count6(self):
        self._test_linux_count('linux6', 1, 4)

    def test_linux_count7(self):
        self._test_linux_count('linux7', 1, 2)

    def test_linux_count8(self):
        self._test_linux_count('linux8', 2, 2)

    def test_linux_count9(self):
        self._test_linux_count('linux9', 2, 4)

if __name__ == '__main__':
    unittest.main()
