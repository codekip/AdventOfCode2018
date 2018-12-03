import os
from itertools import cycle, accumulate


def read_input(input):
    return [int(x) for x in input.split("\n")]


def twice_reddit(data):
    seen = set()
    return next(f for f in accumulate(cycle(data)) if f in seen or seen.add(f))


# this function is equivalent to the one above
def twice(data):
    seen = set()
    for running_total in accumulate(cycle(data)):
        if running_total in seen:
            return (
                running_total
            )  # replacing return with yield makes it a generator, so you need to wrap the caller with next()
        else:
            seen.add(running_total)


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        input = read_input(f.read().strip())
        print("part one ", twice(input))


if __name__ == "__main__":
    main()
