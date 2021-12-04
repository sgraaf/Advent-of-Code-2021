#!/usr/bin/env python
# coding: utf-8
import re
from typing import List

from aoc_utils import read, to_lines

print("--- Day 4: Giant Squid ---")

# read the input data from `input.txt`
data = filter(None, to_lines(read("input.txt")))

# parse input data
numbers = list(map(int, next(data).split(",")))
boards = []
board = []
for i, line in enumerate(data):
    board.append(list(map(int, re.findall(r"\d+", line))))
    if (i + 1) % 5 == 0:
        boards.append(board)
        board = []


def update_board(board: List[List[int]], n: int) -> None:
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == n:
                board[i][j] = -1


def board_wins(board: List[List[int]]) -> bool:
    for row in board:
        if sum(row) == -5:
            return True
    for i in range(len(board[0])):
        col = [row[i] for row in board]
        if sum(col) == -5:
            return True
    return False


def compute_score(board: List[List[int]], n: int) -> int:
    score = 0
    for row in board:
        for col in row:
            if col != -1:
                score += col
    return score * n


# part one
print("--- Part One ---")
boards_won = []
board_to_number = {}
for n in numbers:
    for i, board in enumerate(boards):
        if i not in boards_won:
            update_board(board, n)
            if board_wins(board):
                boards_won.append(i)
                board_to_number[i] = n

print(compute_score(boards[boards_won[0]], board_to_number[boards_won[0]]))


# part two
print("--- Part Two ---")
print(compute_score(boards[boards_won[-1]], board_to_number[boards_won[-1]]))
