#!/usr/bin/env python
# coding: utf-8
from aoc_utils import read, to_lines

print("--- Day 10: Syntax Scoring ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# part one
print("--- Part One ---")
chunk_close_to_open = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
chunk_close_to_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

syntax_error_score = 0
good_lines = []
for line in data:
    c_stack = []
    for c in line:
        if c in set(chunk_close_to_open.values()):  # opening of chunk
            c_stack.append(c)
        elif c in set(chunk_close_to_open.keys()):  # closing of chunk
            if c_stack.pop() != chunk_close_to_open[c]:
                print(c, c_stack[-1])
                syntax_error_score += chunk_close_to_points[c]
                break
    else:
        good_lines.append(line)

print(syntax_error_score)

# part two
print("--- Part Two ---")
chunk_close_to_points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}
completion_scores = []
for line in good_lines:
    completion_score = 0
    c_stack = []
    for c in line:
        if c in set(chunk_close_to_open.values()):  # opening of chunk
            c_stack.append(c)
        elif c in set(chunk_close_to_open.keys()):  # closing of chunk
            c_stack.pop()

    for c in c_stack[::-1]:
        completion_score *= 5
        completion_score += chunk_close_to_points[c]

    completion_scores.append(completion_score)

# sort completion scores
completion_scores = sorted(completion_scores)

print(completion_scores[len(completion_scores) // 2])
