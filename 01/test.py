import unittest
from code import *


class TestCase(unittest.TestCase):

    def test_a(self):
        self.assertEqual(calculate(['+1']), 1)
        self.assertEqual(calculate(['+15']), 15)
        self.assertEqual(calculate(['+15\n', '-14\n']), 1)

    def test_add(self):
        self.assertEqual(add([1, 3, 3]), 7)

    def test_input(self):
        self.assertEqual(calculate(openfile()), 439)


if __name__ == "__main__":
    unittest.main()
