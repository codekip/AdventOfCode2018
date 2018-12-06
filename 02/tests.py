import unittest
from code import *


class TestPartOne(unittest.TestCase):
    def test_count_repetitions(self):
        self.assertEqual(count_repetitions("abcdef"), {"twice": 0, "three": 0})
        self.assertEqual(count_repetitions("bababc"), {"twice": 1, "three": 1})
        self.assertEqual(count_repetitions("abbcde"), {"twice": 1, "three": 0})
        self.assertEqual(count_repetitions("abcccd"), {"twice": 0, "three": 1})
        self.assertEqual(count_repetitions("aabcdd"), {"twice": 1, "three": 0})
        self.assertEqual(count_repetitions("abcdee"), {"twice": 1, "three": 0})
        self.assertEqual(count_repetitions("ababab"), {"twice": 0, "three": 1})

    def test_list(self):
        lss = "abcdef\nbababc\nabbcde\nabcccd\naabcdd\nabcdee\nababab"
        self.assertEqual(result(lss), 12)

    def test_part_two(self):
        line = "abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz"
        self.assertEqual(common_letters(line), "fgij")


if __name__ == "__main__":
    unittest.main()
