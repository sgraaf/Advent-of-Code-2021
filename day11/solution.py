#!/usr/bin/env python
# coding: utf-8
from itertools import count
from typing import List, Set, Tuple

from aoc_utils import find_neighbouring_indices, read, to_lines

print("--- Day 11: Dumbo Octopus ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# parse the input data
data = [[int(c) for c in item] for item in data]


def contains_greater_than_9(data: List[List[int]], has_flashed: Set[Tuple[int, int]]):
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if (i, j) not in has_flashed and val > 9:
                return True
    return False


# part one
print("--- Part One ---")
flash_count = 0
n = 100
for step in range(n):
    # increment each val with 1
    for i, row in enumerate(data):
        for j in range(len(row)):
            data[i][j] += 1

    # flash
    has_flashed = set()
    while contains_greater_than_9(data, has_flashed):
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                if (i, j) not in has_flashed and val > 9:  # flash time babyyy
                    for i_, j_ in find_neighbouring_indices(i, j, len(data), len(row)):
                        data[i_][j_] += 1
                    has_flashed.add((i, j))

    # set flashed to 0
    for i, j in has_flashed:
        data[i][j] = 0

    # update flash count
    flash_count += len(has_flashed)

print(flash_count)

# part two
print("--- Part Two ---")
for step in count(n + 1):
    # increment each val with 1
    for i, row in enumerate(data):
        for j in range(len(row)):
            data[i][j] += 1

    # flash
    has_flashed = set()
    while contains_greater_than_9(data, has_flashed):
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                if (i, j) not in has_flashed and val > 9:  # flash time babyyy
                    for i_, j_ in find_neighbouring_indices(i, j, len(data), len(row)):
                        data[i_][j_] += 1
                    has_flashed.add((i, j))

    # set flashed to 0
    for i, j in has_flashed:
        data[i][j] = 0

    # check if all octopi have flashed
    if len(has_flashed) == len(data) * len(data[0]):
        print(step)
        break
