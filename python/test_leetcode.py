import importlib.util
import unittest

_FILENAME = '436-find-right-interval.py'

spec = importlib.util.spec_from_file_location("module.name", _FILENAME)
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)


class MyTest(unittest.TestCase):
    def setUp(self):
        self.s = foo.Solution()

    def test(self):
        self.assertEqual(
            [-1, 0, 1],
            self.s.findRightInterval([[3, 4], [2, 3], [1, 2]])
        )
        self.assertEqual(
            [-1, 2, -1],
            self.s.findRightInterval([[1, 4], [2, 3], [3, 4]])
        )
        self.assertEqual(
            [3, 3, 3, 4, 5, -1],
            self.s.findRightInterval([[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]])
        )


if __name__ == '__main__':
    unittest.main()
