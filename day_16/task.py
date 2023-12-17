# task 1
import copy
import sys
import numpy as np
from functools import lru_cache

sys.setrecursionlimit(10000)

# Read file
with open('input.txt', 'r') as file:
    data = file.readlines()
    # Remove newlines
    data = [line.strip() for line in data]

height = len(data)
width = len(data[0])

energized_array = np.zeros((height, width))
# Tracks whether we have been to a position before
repetition_list = set()

# Direction handling dictionary
direction_mapping = {
    '/': {'up': ('right', 1, 0), 'down': ('left', -1, 0), 'left': ('down', 0, 1), 'right': ('up', 0, -1)},
    '\\': {'up': ('left', -1, 0), 'down': ('right', 1, 0), 'left': ('up', 0, -1), 'right': ('down', 0, 1)},
    '|': {'up': ('up', 0, -1), 'down': ('down', 0, 1)},
    '-': {'left': ('left', -1, 0), 'right': ('right', 1, 0)}
}


# Need a recursive function that finds all energized positions
def search(x, y, direction):
    # Avoid repetitive recursive calls
    if (x, y, direction) in repetition_list or x < 0 or x >= width or y < 0 or y >= height:
        return 0

    # Check if we have already energized this position
    energized = 1 - energized_array[y][x]
    energized_array[y][x] = 1

    # Get the current symbol
    symbol = data[y][x]

    repetition_list.add((x,y,direction))

    # Process based on symbol
    if symbol in direction_mapping:
        if direction in direction_mapping[symbol]:
            new_direction, dx, dy = direction_mapping[symbol][direction]
            energized += search(x + dx, y + dy, new_direction)
        else:
            # For '|' and '-', handling the perpendicular directions
            if symbol in '|-':
                for dir in ['up', 'down'] if symbol == '|' else ['left', 'right']:
                    new_direction, dx, dy = direction_mapping[symbol][dir]
                    energized += search(x + dx, y + dy, new_direction)
    else:
        # For any other symbol, continue in the same direction
        dir_mappings = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
        dx, dy = dir_mappings[direction]
        energized += search(x + dx, y + dy, direction)

    return energized


print(search(0,0,'right'))


# Task 2
# Find the start position that gives the most energized grid
most_energized = 0
for i in range(height):
    energized_array = np.zeros((height, width))
    repetition_list.clear()
    most_energized = max(most_energized, search(0, i, 'right'))
    most_energized = max(most_energized, search(width-1, i, 'left'))
    print(i)
for j in range(width):
    energized_array = np.zeros((height, width))
    repetition_list.clear()
    most_energized = max(most_energized, search(j, 0, 'down'))
    most_energized = max(most_energized, search(j, height-1, 'up'))
    print(j)

print(most_energized)


