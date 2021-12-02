#!/usr/bin/env python
# coding: utf-8
import re

from aoc_utils import read, to_lines

print("--- Day 2: Dive! ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# parse the input data
commands = []
for line in data:
    direction, amount = re.match(r"(\w+) (\d+)", line).groups()
    commands.append((direction, int(amount)))

# part one
print("--- Part One ---")
x, y = 0, 0
for direction, amount in commands:
    if direction == "forward":
        x += amount
    elif direction == "up":
        y -= amount
    elif direction == "down":
        y += amount

print(x * y)

# part two
print("--- Part Two ---")
x, y, aim = 0, 0, 0
for direction, amount in commands:
    if direction == "forward":
        x += amount
        y += aim * amount
    elif direction == "up":
        aim -= amount
    elif direction == "down":
        aim += amount

print(x * y)
