# Read file
import copy
import hashlib
import sys
from functools import lru_cache

sys.setrecursionlimit(30000)

import numpy as np

with open("input.txt", "r") as file:
    data = file.readlines()

# Create 2d array
data = [list(line.strip()) for line in data]

height = len(data)
width = len(data[0])

end = (width-2, height-1)

steps_grid = np.zeros((height, width), dtype=bool)

slopes = ['>', '<', '^', 'v']
slope_directions = {
    '<': (-1, 0),
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1)
}
directions = {
    (1, 0): 'right',
    (-1, 0): 'left',
    (0, -1): 'up',
    (0, 1): 'down'
}

neighbours = []
for y in range(height):
    row = []
    for x in range(width):
        close_neighbours = []
        for dx, dy in slope_directions.values():
            if 0 <= x + dx < width and 0 <= y + dy < height and data[y + dy][x + dx] != '#':
                close_neighbours.append((x + dx, y + dy))
        row.append(close_neighbours)
    neighbours.append(row)


def hash_array_sha256(arr):
    arr_bytes = arr.tobytes()
    return hashlib.sha256(arr_bytes).hexdigest()


# task 1 and 2
def traverse_path(x, y, step_grid, slope=True):
    if step_grid[y][x] == 1:
        return False, 0

    step_grid[y][x] = 1
    path_value = 0
    valid_path = False

    if (x, y) == end:
        step_grid[y][x] = 0
        return True, 0

    if slope and data[y][x] in slopes:
        dx, dy = slope_directions[data[y][x]]
        if step_grid[y + dy][x + dx] == 0:
            valid_path, path_value = traverse_path(x + dx, y + dy, step_grid, slope=slope)

        step_grid[y][x] = 0
        return valid_path, path_value + 1

    possible_neighbours = neighbours[y][x]
    # Remove neighbours that are already visited
    #possible_neighbours = [neighbour for neighbour in possible_neighbours if step_grid[neighbour[1]][neighbour[0]] == 0]

    #if len(possible_neighbours) == 1:
        #valid_path, path_value = traverse_path(possible_neighbours[0][0], possible_neighbours[0][1], step_grid, slope=slope)

    #else:

    for close_neighbour in possible_neighbours:
        neighbour_x, neighbour_y = close_neighbour
        #hashed_array = hash_array_sha256(step_grid)
        #if not (neighbour_x, neighbour_y, hashed_array) in cache:
            #cache[(neighbour_x, neighbour_y, hashed_array)] = traverse_path(neighbour_x, neighbour_y, step_grid, slope=slope)

        #temp_valid_path, temp_path_value = cache[(neighbour_x, neighbour_y, hashed_array)]
        temp_valid_path, temp_path_value = traverse_path(neighbour_x, neighbour_y, step_grid, slope=slope)
        if temp_valid_path:
            path_value = max(path_value, temp_path_value)
            valid_path = True

    steps_grid[y][x] = 0
    return valid_path, path_value + 1


print(traverse_path(1, 0, steps_grid, slope=True))
steps_grid = np.zeros((height, width), dtype=bool)
#print(traverse_path(1, 0, steps_grid, slope=False))

# task 2

# Try iterative approach
queue = [(1,0,0,steps_grid)]
max_steps = 0
cache = {}
while queue:
    x, y, steps, step_grid = queue.pop(0)

    while (x, y) != end:

        steps += 1
        step_grid[y][x] = 1
        possible_neighbours = neighbours[y][x]
        # Remove neighbours that are already visited
        close_neighbours = [neighbour for neighbour in possible_neighbours if step_grid[neighbour[1]][neighbour[0]] == 0]
        if len(close_neighbours) == 0:
            break
        elif len(close_neighbours) == 1:
            x, y = close_neighbours[0]
            continue
        else:
            # Add all neighbours expect the first to the queue
            for neighbour in close_neighbours[1:]:
                queue.append((neighbour[0], neighbour[1], steps, copy.deepcopy(step_grid)))
            x, y = close_neighbours[0]

    if (x, y) == end:
        max_steps = max(max_steps, steps)
        print(len(queue))


print(max_steps)



