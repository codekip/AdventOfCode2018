import os
from collections import defaultdict, OrderedDict
import itertools


def count_repetitions(str):
    ans = OrderedDict()
    count = defaultdict(int)
    for letter in str:
        count[letter] += 1

    twice = list(filter(lambda x: x == 2, count.values()))
    three = list(filter(lambda x: x == 3, count.values()))

    ans["twice"] = 1 if len(twice) > 0 else 0
    ans["three"] = 1 if len(three) > 0 else 0

    return dict(ans)


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
    sortedwords = list()
    good_words = list()

    for line in all:
        ans = result(line, test_number=2)
        if ans["twice"] > 0 or ans["three"] > 0:
            sortedwords.append("".join(sorted(line)))

    unique = set(sortedwords)
    for a, b in itertools.combinations(unique, 2):
        letter_not_in_a_or_b = set(a).symmetric_difference(set(b))
        if len(letter_not_in_a_or_b) == 1:
            print(a, b, letter_not_in_a_or_b)
            return set(a).intersection(set(b))


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        input = f.read()
        # print(common_letters(input))


if __name__ == "__main__":
    main()
