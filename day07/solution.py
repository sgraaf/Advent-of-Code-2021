#!/usr/bin/env python
# coding: utf-8
from aoc_utils import read

print("--- Day 7: The Treachery of Whales ---")

# read the input data from `input.txt`
data = list(map(int, read("input.txt").split(",")))

# part one
print("--- Part One ---")
least_fuel = 0
for pos in range(min(data), max(data) + 1):
    total_fuel = 0
    for crab_pos in data:
        total_fuel += abs(crab_pos - pos)
    if total_fuel < least_fuel or least_fuel == 0:
        least_fuel = total_fuel

print(least_fuel)

# part two
print("--- Part Two ---")
least_fuel = 0
for pos in range(min(data), max(data) + 1):
    total_fuel = 0
    for crab_pos in data:
        if crab_pos == pos:
            continue
        total_fuel += sum(i for i in range(1, abs(crab_pos - pos) + 1))
    if total_fuel < least_fuel or least_fuel == 0:
        least_fuel = total_fuel

print(least_fuel)
