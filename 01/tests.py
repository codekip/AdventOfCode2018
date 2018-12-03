import unittest
from code import *


class TestPartTwo(unittest.TestCase):
    def test_part_two(self):
        self.assertEqual(twice([+3, +3, +4, -2, -4]), 10)
        self.assertEqual(twice(main()), 10)
    

if __name__ == "__main__":
    unittest.main()
