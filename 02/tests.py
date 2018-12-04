import unittest
from code import *


class TestPartOne(unittest.TestCase):
    def test_count_repetitions(self):
        # self.assertEqual(count_repetitions("abcdef"), {"abcdef": {"2": 0, "3": 0}})
        # self.assertEqual(count_repetitions("bababc"), {"bababc": {"2": 1, "3": 1}})
        # self.assertEqual(count_repetitions("abbcde"), "b")
        # self.assertEqual(count_repetitions("abcdef"), None)
        self.assertEqual(count_repetitions("abbbccde"), "b")
        # self.assertEqual(count_repetitions("abcccd"), None)


if __name__ == "__main__":
    unittest.main()
