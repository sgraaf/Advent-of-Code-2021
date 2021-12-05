#!/usr/bin/env python
# coding: utf-8
import re
from collections import defaultdict
from typing import List, Tuple

from aoc_utils import read, to_lines

print("--- Day 5: Hydrothermal Venture ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# parse the input data
lines = []
for line in data:
    x1, y1, x2, y2 = map(int, re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line).groups())
    lines.append((x1, y1, x2, y2))


def compute_num_overlapping_points(
    lines: List[Tuple[int, int, int, int]], use_diagonals: bool = False
) -> int:
    coordinate_to_count = defaultdict(int)
    for x1, y1, x2, y2 in lines:
        if x1 == x2:
            for y in range(y1, y2 + 1 if y2 > y1 else y2 - 1, 1 if y2 > y1 else -1):
                coordinate_to_count[(x1, y)] += 1
        elif y1 == y2:
            for x in range(x1, x2 + 1 if x2 > x1 else x2 - 1, 1 if x2 > x1 else -1):
                coordinate_to_count[(x, y1)] += 1
        elif use_diagonals:
            for x in range(x1, x2 + 1 if x2 > x1 else x2 - 1, 1 if x2 > x1 else -1):
                for y in range(y1, y2 + 1 if y2 > y1 else y2 - 1, 1 if y2 > y1 else -1):
                    if abs(x - x1) == abs(y - y1):
                        coordinate_to_count[(x, y)] += 1

    return len([x for x in coordinate_to_count.values() if x >= 2])


# part one
print("--- Part One ---")
print(compute_num_overlapping_points(lines))

# part two
print("--- Part Two ---")
print(compute_num_overlapping_points(lines, use_diagonals=True))
