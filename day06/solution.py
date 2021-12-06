#!/usr/bin/env python
# coding: utf-8
from collections import deque

from aoc_utils import read

print("--- Day 6: Lanternfish ---")

# read the input data from `input.txt`
data = list(map(int, read("input.txt").split(",")))

# part one
print("--- Part One ---")
# naive approach
fishes = data.copy()
t = 80
for _ in range(t):
    for i in range(0, len(fishes)):
        if fishes[i] == 0:
            fishes.append(8)
            fishes[i] = 6
        else:
            fishes[i] = fishes[i] - 1

print(len(fishes))

# part two
print("--- Part Two ---")
# smart approach
# use a deque for fast `.pop(0)` a.k.a. `.popleft()`
fishes_days = deque([data.count(i) for i in range(0, 9)])
t = 256
for _ in range(t):
    new_fish = fishes_days.popleft()
    fishes_days[-2] += new_fish
    fishes_days.append(new_fish)

print(sum(fishes_days))
