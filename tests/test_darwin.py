# This file is part of cpu_cores released under the MIT license.
# See the LICENSE file for more information.

import unittest
import os

from cpu_cores import CPUCoresCounter


class TestCPUCores(unittest.TestCase):

    def _dir(self):
        return os.path.dirname(__file__)

    def test_factory_darwin(self):
        x = CPUCoresCounter.factory(force_platform='darwin')
        self.assertTrue(x is not None)
        self.assertTrue(x.platform is not None)
        self.assertTrue(x.platform == 'darwin')

    def _test_darwin_count(self):
        x = CPUCoresCounter.factory(force_platform='darwin')
        self.assertTrue(x is not None)
        self.assertTrue(x.platform is not None)
        self.assertTrue(x.platform == 'darwin')
        return x

    def test_darwin_count1(self):
        x = self._test_darwin_count()
        x._count('cat %s' % os.path.join(self._dir(), 'darwin1'))
        self.assertEqual(x._physical_cores_count, 2)
        self.assertEqual(x._physical_processors_count, 1)


if __name__ == '__main__':
    unittest.main()
