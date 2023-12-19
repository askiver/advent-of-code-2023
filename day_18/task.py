# Read the file
import numpy as np
import sys
# Set the recursion limit to 10000
sys.setrecursionlimit(10000)
with open("input.txt") as f:
    lines = f.readlines()
    # Remove the newline character
    lines = [line.strip() for line in lines]

# Task 1

# Dictionary of directions and their coordinates
directions = {
    "U": (0, -1),
    "D": (0, 1),
    "R": (1, 0),
    "L": (-1, 0)
}

grid = np.zeros((1000, 1000))
x = 500
y = 500
grid[x, y] = 1

# Fill in the grid

for line in lines:
    # split on space
    line = line.split(" ")
    direction = line[0]
    steps = int(line[1])
    for i in range(steps):
        x += directions[direction][0]
        y += directions[direction][1]
        grid[x, y] = 1

# flood fill algorithm
def iterative_flood_fill(x, y, fill_value=1):
    # Create a stack with the starting point
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()  # Pop the last item

        # Check bounds
        if x < 0 or x >= grid.shape[1] or y < 0 or y >= grid.shape[0]:
            continue

        # Check if already filled or is a boundary
        if grid[y, x] == fill_value:
            continue

        # Fill the position
        grid[y, x] = fill_value

        # Add the neighboring positions to the stack
        stack.append((x + 1, y))  # Right
        stack.append((x - 1, y))  # Left
        stack.append((x, y + 1))  # Down
        stack.append((x, y - 1))  # Up


iterative_flood_fill(502, 502)

print(np.sum(grid))

# Task 2

dig_instructions = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}


perimeter, shoelace = 0, 0
x, y, pts = 0, 0, [(0, 0)]
for line in lines:
    # split on space
    line = line.split(" ")
    instruction = line[2]
    steps = int(instruction[2:-2], 16)
    direction = dig_instructions[instruction[-2]]


    dx, dy = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}[direction]
    x, y = x + dx * steps, y + dy * steps
    pts.append((x, y))
    perimeter += steps

shoelace = sum((a[0] * b[1] - b[0] * a[1]) for a, b in zip(pts, pts[1:])) // 2
print(shoelace + perimeter // 2 + 1)






