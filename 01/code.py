import operator
import os
import sys
from functools import reduce
from itertools import accumulate, cycle

'''
# Part 2
from itertools import accumulate, cycle
seen = set()
print(next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f)))
'''


def calculate(data, thefunc=''):
    no_newline = [x.split('\n') for x in data]
    flat = list(filter(lambda x: x != '', [
                item for sublist in no_newline for item in sublist]))
    if thefunc != '':
        return thefunc(flat)
    else:
        return flat


def add(lst):
    return reduce(lambda x, y: int(x) + int(y), lst, 0)


def add_acc(lst):
    return lambda x, y: int(x) + int(y), lst


def twice(lst):
    data = calculate(lst)
    return 0


def doit(data):
    pass


def openfile():
    inputfile = os.path.join(sys.path[0], 'input.txt')
    with open(inputfile, 'r') as file:
        return file.readlines()
