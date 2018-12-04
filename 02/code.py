import os
from collections import Counter, defaultdict


def count_repetitions(str):
    cnt = Counter(str)
    filtered = dict(filter(lambda x: x[1] in [2, 3], cnt.items()))
    print(filtered)


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        input = f.read()


if __name__ == "__main__":
    main()
