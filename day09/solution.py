#!/usr/bin/env python
# coding: utf-8
from functools import reduce
from operator import mul

from aoc_utils import find_neighbouring_indices, read, to_lines

print("--- Day 9: Smoke Basin ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# parse the input data
data = [list(map(int, list(s))) for s in data]

# part one
print("--- Part One ---")
low_points = {}
for i, row in enumerate(data):
    for j, val in enumerate(row):
        neighbouring_indices = find_neighbouring_indices(i, j, len(data), len(row))
        neighbouring_vals = [data[i][j] for i, j in neighbouring_indices]

        if val < min(neighbouring_vals):
            low_points[(i, j)] = val

print(sum(low_points.values()) + len(low_points))

# part two
print("--- Part Two ---")
basin_sizes = []
for (i_low_point, j_low_point), val_low_point in low_points.items():
    basin = [(i_low_point, j_low_point, val_low_point)]

    points_to_check = [(i_low_point, j_low_point)]
    while points_to_check:
        i_point, j_point = points_to_check.pop()
        val_point = data[i_point][j_point]

        neighbouring_indices = find_neighbouring_indices(
            i_point, j_point, len(data), len(data[0])
        )

        for i_neighbour, j_neighbour in neighbouring_indices:
            val_neighbour = data[i_neighbour][j_neighbour]
            if (
                i_neighbour,
                j_neighbour,
                val_neighbour,
            ) not in basin and val_point < val_neighbour < 9:
                points_to_check.append((i_neighbour, j_neighbour))
                basin.append((i_neighbour, j_neighbour, val_neighbour))

    basin_sizes.append(len(basin))

# sort basin_sizes by... size
basin_sizes = sorted(basin_sizes, reverse=True)

print(reduce(mul, basin_sizes[:3]))
