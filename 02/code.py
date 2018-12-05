import os
from collections import defaultdict, OrderedDict


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


def result(lst):
    twos = 0
    threes = 0

    all = lst.split("\n")
    for item in all:
        ans = count_repetitions(item)
        twos += ans["twice"]
        threes += ans["three"]

    return twos * threes


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        input = f.read()
        print(result(input))


if __name__ == "__main__":
    main()
