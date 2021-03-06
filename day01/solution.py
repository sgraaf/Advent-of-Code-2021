#!/usr/bin/env python
# coding: utf-8
from aoc_utils import read, to_numbers

print("--- Day 1: Sonar Sweep ---")

# read the input data from `input.txt`
data = to_numbers(read("input.txt"))

# part one
print("--- Part One ---")
print(sum(measurement > data[i - 1] for i, measurement in enumerate(data)))

# part two
print("--- Part Two ---")
print(sum(sum(data[i - 2 : i + 1]) > sum(data[i - 3 : i]) for i in range(3, len(data))))
