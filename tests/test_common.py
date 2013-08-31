# This file is part of cpu_cores released under the MIT license.
# See the LICENSE file for more information.

import unittest
from cpu_cores import CPUCoresCounter


class TestCommon(unittest.TestCase):

    def test_factory(self):
        x = CPUCoresCounter.factory()
        self.assertTrue(x is not None)
        self.assertTrue(x.platform is not None)
        self.assertTrue(len(x.platform) > 0)

    def _test_unkwown_platform(self):
        CPUCoresCounter.factory(force_platform='unknown')

    def _test_bad_call(self):
        x = CPUCoresCounter()
        x._count()

    def test_unknown_platform(self):
        self.assertRaises(NotImplementedError, self._test_unkwown_platform)

    def test_bad_call(self):
        self.assertRaises(NotImplementedError, self._test_bad_call)

    def _test_get_common(self):
        x = CPUCoresCounter.factory()
        self.assertTrue(x is not None)
        self.assertTrue(x.platform is not None)
        self.assertTrue(len(x.platform) > 0)
        return x

    def test_get_physical_cores_count(self):
        x = self._test_get_common()
        c = x.get_physical_cores_count()
        self.assertTrue(c > 0)

    def test_get_physical_processors_count(self):
        x = self._test_get_common()
        c = x.get_physical_processors_count()
        self.assertTrue(c > 0)


if __name__ == '__main__':
    unittest.main()
