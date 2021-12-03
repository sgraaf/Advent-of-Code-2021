#!/usr/bin/env python
# coding: utf-8
from typing import Callable, List

from aoc_utils import read, to_lines

print("--- Day 3: Binary Diagnostic ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# part one
print("--- Part One ---")
gamma_rate = ""
epsilon_rate = ""
for i in range(len(data[0])):
    cs = [l[i] for l in data]
    gamma_rate += max(cs, key=cs.count)
    epsilon_rate += min(cs, key=cs.count)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# part two
print("--- Part Two ---")


def find_rating(data: List[str], func: Callable) -> str:
    data = data.copy()
    for i in range(len(data[0])):
        cs = [l[i] for l in data]
        if func == max:
            c = "1" if cs.count("1") >= cs.count("0") else "0"
        else:
            c = "0" if cs.count("0") <= cs.count("1") else "1"
        data = [x for x in data if x[i] == c]
        if len(data) == 1:
            return data.pop()


oxygen_generator_rating = find_rating(data, max)
co2_scrubber_rating = find_rating(data, min)

print(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))
