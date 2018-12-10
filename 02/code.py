import difflib
import itertools
import os
from collections import defaultdict

def count_repetitions(str):
    ans = dict()
    count = defaultdict(int)
    for letter in str:
        count[letter] += 1

    twice = list(filter(lambda x: x == 2, count.values()))
    three = list(filter(lambda x: x == 3, count.values()))

    ans["twice"] = 1 if len(twice) > 0 else 0
    ans["three"] = 1 if len(three) > 0 else 0

    return ans

def result(lst, test_number=1):
    twos = 0
    threes = 0

    all = lst.split("\n")
    for item in all:
        ans = count_repetitions(item)
        twos += ans["twice"]
        threes += ans["three"]

    if test_number == 1:
        return twos * threes
    else:
        return ans


def common_letters(lst):
    all = lst.split("\n")
    for a, b in itertools.combinations(all, 2):
        if len([li for li in difflib.ndiff(a, b) if li[0] != " "]) == 2:
            print(a, b, [li for li in difflib.ndiff(a, b) if li[0] != " "])


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        input = f.read()
        print(common_letters(input))


if __name__ == "__main__":
    main()
