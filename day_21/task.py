# Read file
import numpy as np
from functools import lru_cache

with open("input.txt") as f:
    lines = f.readlines()

# create 2d array
grid = []
for line in lines:
    grid.append(list(line.strip()))

# Task 1

height = len(grid)
width = len(grid[0])

step_grid = np.zeros((height, width), dtype=int)

# Find index of S
start = None
for i in range(height):
    for j in range(width):
        if grid[i][j] == 'S':
            start = (j, i)

@lru_cache(maxsize=None)
def find_neighbours(x, y, step):
    if step == 0:
        step_grid[y][x] = 1
        return
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + dx < width and 0 <= y + dy < height and grid[y + dy][x + dx] != '#':
            find_neighbours(x + dx, y + dy, step - 1)


find_neighbours(start[0], start[1], 64)

print(np.sum(step_grid))
