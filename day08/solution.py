#!/usr/bin/env python
# coding: utf-8
import re

from aoc_utils import read, to_lines

print("--- Day 8: Seven Segment Search ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# parse the input data
data = [item.split(" | ") for item in data]

# part one
print("--- Part One ---")
easy_digit_count = 0
for _, output_values in data:
    for output_value in re.findall(r"[a-z]+", output_values):
        if len(output_value) in {2, 3, 4, 7}:
            easy_digit_count += 1

print(easy_digit_count)

# part two
print("--- Part Two ---")
output_values_sum = 0
for signal_patterns, output_values in data:
    # sort signal patterns by length
    signal_patterns = sorted(re.findall(r"[a-z]+", signal_patterns), key=len)

    signal_pattern_map = {}
    for signal_pattern in map(set, signal_patterns):
        if len(signal_pattern) == 2:  # 1
            value = 1
        elif len(signal_pattern) == 3:  # 7
            value = 7
        elif len(signal_pattern) == 4:  # 4
            value = 4
        elif len(signal_pattern) == 5:  # 2, 3 or 5
            if len(signal_pattern & signal_pattern_map[7]) == 3:  # 3
                value = 3
            elif len(signal_pattern & signal_pattern_map[4]) == 3:  # 5
                value = 5
            else:  # 2
                value = 2
        elif len(signal_pattern) == 6:  # 0, 6 or 9
            if len(signal_pattern & signal_pattern_map[1]) == 1:  # 6
                value = 6
            elif len(signal_pattern & signal_pattern_map[3]) == 5:  # 9
                value = 9
            else:  # 0
                value = 0
        else:  # 8
            value = 8

        signal_pattern_map[value] = signal_pattern

    # parse output values
    output_value = ""
    for output_val in map(set, re.findall(r"[a-z]+", output_values)):
        for value, signal_pattern in signal_pattern_map.items():
            if output_val == signal_pattern:
                output_value += str(value)
                break

    output_values_sum += int(output_value)

print(output_values_sum)
