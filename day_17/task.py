import math
from functools import lru_cache
from collections import defaultdict

import numpy as np
from numpy import inf

# set recursion limit to 10000
import sys
sys.setrecursionlimit(10000)

# Task 1
# Read file
with open("input.txt", "r") as file:
    data = file.read().splitlines()

# Convert each line to a list of integers
data = [list(map(int, list(line))) for line in data]

height = len(data)
width = len(data[0])

print(data)
direction_mapping = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}
available_directions = {
    "up": ["up", "left", "right"],
    "down": ["down", "left", "right"],
    "left": ["left", "up", "down"],
    "right": ["right", "up", "down"],
}

repetition_array = np.zeros((height, width), dtype=int)

def h(current_position):
    return math.sqrt(abs(current_position[0] - width + 1)**2 + abs(current_position[1] - height + 1)**2)

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path

def a_star(start, h):
    open_set = set()
    open_set.add(start)

    came_from = {}

    g_score = defaultdict(lambda: inf)
    g_score[start] = 0

    f_score = defaultdict(lambda: inf)
    f_score[start] = h(start)

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current[0] == width - 1 and current[1] == height - 1:
            return reconstruct_path(came_from, current)
        open_set.remove(current)

        directions = available_directions[current[2]] if current[3] < 3 else available_directions[current[2]][1:]
        for d in directions:
            moves = current[3] + 1 if d == current[2] else 1
            neighbour = (current[0] + direction_mapping[d][0], current[1] + direction_mapping[d][1], d, moves)
            if neighbour[0] < 0 or neighbour[0] >= width or neighbour[1] < 0 or neighbour[1] >= height:
                continue

            tentative_gscore = g_score[current] + data[neighbour[1]][neighbour[0]]
            if tentative_gscore < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_gscore
                f_score[neighbour] = g_score[neighbour] + h(neighbour)
                if neighbour not in open_set:
                    open_set.add(neighbour)

# Task 2
def cursed_a_star(start, h):
    open_set = set()
    open_set.add(start)

    came_from = {}

    g_score = defaultdict(lambda: inf)
    g_score[start] = 0

    f_score = defaultdict(lambda: inf)
    f_score[start] = h(start)

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current[0] == width - 1 and current[1] == height - 1:
            return reconstruct_path(came_from, current)
        open_set.remove(current)

        if current[3] < 4:
            directions = [current[2]]
        elif current[3] < 10:
            directions = available_directions[current[2]]
        else:
            directions = available_directions[current[2]][1:]

        for d in directions:
            moves = current[3] + 1 if d == current[2] else 1
            neighbour = (current[0] + direction_mapping[d][0], current[1] + direction_mapping[d][1], d, moves)
            if neighbour[0] < 0 or neighbour[0] >= width or neighbour[1] < 0 or neighbour[1] >= height:
                continue

            tentative_gscore = g_score[current] + data[neighbour[1]][neighbour[0]]
            if tentative_gscore < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_gscore
                f_score[neighbour] = g_score[neighbour] + h(neighbour)
                if neighbour not in open_set:
                    open_set.add(neighbour)


path = a_star((0,0,'right',0), h)
heat_sum = 0
for p in path[1:]:
    heat_sum += data[p[1]][p[0]]

path = cursed_a_star((0,0,'right',0), h)
heat_sum = 0
for p in path[1:]:
    heat_sum += data[p[1]][p[0]]
print(heat_sum)