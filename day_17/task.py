from functools import lru_cache

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



@lru_cache(maxsize=None)
def search(x, y, direction, moves):
    if x < 0 or x >= width or y < 0 or y >= height:
        return inf
    if repetition_array[y][x] == 1:
        return inf
    if x == width - 1 and y == height - 1:
        print(repetition_array)
        print()
        return data[y][x]

    repetition_array[y][x] = 1
    directions = available_directions[direction] if moves < 3 else available_directions[direction][1:]
    # sort directions by euclidean distance to the end
    directions = sorted(directions, key=lambda d: (abs(x + direction_mapping[d][0] - width + 1)) + (abs(y + direction_mapping[d][1] - height + 1)))
    """
    result = min(
        search(x + direction_mapping[d][0], y + direction_mapping[d][1], d,
               (moves if d == direction else 0) + 1)
        for d in directions
    ) + data[y][x]
    """
    result = inf
    for d in directions:
        result = min(result, search(x + direction_mapping[d][0], y + direction_mapping[d][1], d,
               (moves if d == direction else 0) + 1))
    result += data[y][x]
    repetition_array[y][x] = 0
    return result

print(min(search(1, 0, "right", 1), search(0, 1, "down", 1)))
