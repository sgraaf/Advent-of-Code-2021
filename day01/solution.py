#!/usr/bin/env python
# coding: utf-8
from aoc_utils import read, to_numbers

print("--- Day 1: Sonar Sweep ---")

# read the input data from `input.txt`
data = to_numbers(read("input.txt"))

# part one
print("--- Part One ---")
increased_count = 0
decreased_count = 0
for i, measurement in enumerate(data):
    if i == 0:
        continue
    if measurement > data[i - 1]:
        increased_count += 1
    elif measurement < data[i - 1]:
        decreased_count += 1

print(f"There are {increased_count} measurements larger than the previous measurement.")

# part two
print("--- Part Two ---")
increased_count = 0
decreased_count = 0
for i in range(3, len(data)):
    sliding_window_sum = sum(data[i - 2 : i + 1])
    previous_sliding_window_sum = sum(data[i - 3 : i])
    if sliding_window_sum > previous_sliding_window_sum:
        increased_count += 1
    elif sliding_window_sum < previous_sliding_window_sum:
        decreased_count += 1

print(f"There are {increased_count} sums larger than the previous sum.")
