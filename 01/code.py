import operator
import os
import sys
from functools import reduce


def calculate(data):
    no_newline = [x.split('\n') for x in data]
    flat = list(filter(lambda x: x != '', [
                item for sublist in no_newline for item in sublist]))
    return add(flat)


def add(lst):
    return reduce(lambda x, y: int(x) + int(y), lst, 0)


def openfile():
    inputfile = os.path.join(sys.path[0], 'input.txt')
    with open(inputfile, 'r') as file:
        return file.readlines()
