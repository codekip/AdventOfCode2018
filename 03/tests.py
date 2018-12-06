import unittest
from code import *


class TestPartOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(width("#1 @ 179,662: 16x27"), 16)
        self.assertEqual(left("#1 @ 179,662: 16x27"), 179)
        self.assertEqual(top("#1 @ 179,662: 16x27"), 662)
        self.assertEqual(id("#1 @ 179,662: 16x27"), 1)
        self.assertEqual(area("#1 @ 179,662: 16x27"), 432)
        self.assertEqual(top_left("#1 @ 179,662: 16x27"), (179, 662))
        self.assertEqual(top_right("#1 @ 179,662: 16x27"), (195, 662))
        self.assertEqual(bottom_right("#1 @ 179,662: 16x27"), (195, 689))
        self.assertEqual(bottom_left("#1 @ 179,662: 16x27"), (179, 689))


if __name__ == "__main__":
    unittest.main()
