#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple

from aoc_utils import read, to_lines

print("--- Day 12: Passage Pathing ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# parse the input data
graph: Dict[str, Set[str]] = defaultdict(set)
for line in data:
    a, b = line.split("-")

    # add edge to graph (undirected)
    graph[a].add(b)
    graph[b].add(a)

print("--- Part One ---")
def find_all_paths(graph: Dict[str, Set[str]], start: str, end: str) -> List[List[str]]:
    # intialize empty list to store paths from start to end
    all_paths = []

    # initialize empty deque to store paths to evaluate
    q = deque()

    # add start node to path and add path to deque
    path = [start]
    q.append(path.copy())

    while q:
        path = q.popleft()
        v = path[-1]

        if v == end:  # path from start to end
            all_paths.append(path)
        else:
            for next_v in graph[v]:
                if next_v not in path or next_v.isupper():
                    new_path = path.copy()
                    new_path.append(next_v)
                    q.append(new_path)

    return all_paths

all_paths = find_all_paths(graph, "start", "end")
print(len(all_paths))

# part two
print("--- Part Two ---")
small_caves = {v for v in graph.keys() if v.islower() and v not in {"start", "end"}}

def find_all_paths_2(graph: Dict[str, Set[str]], start: str, end: str) -> Set[Tuple[str]]:
    # intialize empty list to store paths from start to end
    all_paths = set()

    for small_cave in small_caves:
        # initialize empty deque to store paths to evaluate
        q = deque()

        # add start node to path and add path to deque
        path = [start]
        q.append(path.copy())

        while q:
            path = q.popleft()
            v = path[-1]

            if v == end:  # path from start to end
                all_paths.add(tuple(path))
            else:
                for next_v in graph[v]:
                    if next_v not in path or next_v.isupper() or (next_v == small_cave and path.count(next_v) <= 1):
                        new_path = path.copy()
                        new_path.append(next_v)
                        q.append(new_path)

    return all_paths

all_paths_2 = find_all_paths_2(graph, "start", "end")
print(len(all_paths_2))
