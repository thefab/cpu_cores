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

    def _test_linux_count(self):
        x = CPUCoresCounter.factory(force_platform='linux')
        self.assertTrue(x is not None)
        self.assertTrue(x.platform is not None)
        self.assertTrue(x.platform == 'linux')
        return x

    def test_linux_count1(self):
        x = self._test_linux_count()
        x._count('%s/linux1' % self._dir())
        self.assertEqual(x._physical_cores_count, 4)
        self.assertEqual(x._physical_processors_count, 2)

    def test_linux_count2(self):
        x = self._test_linux_count()
        x._count('%s/linux2' % self._dir())
        self.assertEqual(x._physical_cores_count, 1)
        self.assertEqual(x._physical_processors_count, 1)

    def test_linux_count3(self):
        x = self._test_linux_count()
        x._count('%s/linux3' % self._dir())
        self.assertEqual(x._physical_cores_count, 8)
        self.assertEqual(x._physical_processors_count, 2)


if __name__ == '__main__':
    unittest.main()
