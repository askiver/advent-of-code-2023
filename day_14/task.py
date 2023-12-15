import copy

from tqdm import tqdm

# Task 1

# Read input
with open("input.txt", "r") as file:
    input = file.readlines()

# Remove newlines
input = [line.strip() for line in input]
# Create 2d list of columns
grid = []
for i in range(len(input[0])):
    grid.append([])

for row in range(len(input)):
    for column in range(len(input[row])):
        grid[column].append(input[row][column])
print(grid)


def tilt_rocks(column, north_or_west=True):
    # Check if there are any cube-shaped rocks
    if not column:
        return []
    if "#" not in column:
        return sorted(column, reverse=north_or_west)
    else:
        index = column.index("#")

        # check if the cube-shaped rock is the last one
        if index == len(column) - 1:
            return sorted(column[:index], reverse=north_or_west) + ['#']
        # Check if the cube shaped rock is the first one
        if index == 0:
            return ['#'] + tilt_rocks(column[index + 1:], north_or_west)
        return sorted(column[:index], reverse=north_or_west) + ['#'] + tilt_rocks(column[index + 1:], north_or_west)


new_grid = []

for column in grid:
    new_grid.append(tilt_rocks(column))
sum = 0
for column in new_grid:
    for i in range(len(column)):
        if list(reversed(column))[i] == "O":
            sum += i + 1

print(sum)


# Task 2

def transpose_list(matrix):
    return [list(row) for row in zip(*matrix)]

all_grids = []
for i in tqdm(range(2000)):
    for j in range(len(grid)):
        grid[j] = (tilt_rocks(grid[j], True))
    grid = transpose_list(grid)
    for j in range(len(grid)):
        grid[j] = (tilt_rocks(grid[j], True))
    grid = transpose_list(grid)
    for j in range(len(grid)):
        grid[j] = (tilt_rocks(grid[j], False))
    grid = transpose_list(grid)
    for j in range(len(grid)):
        grid[j] = (tilt_rocks(grid[j], False))
    grid = transpose_list(grid)
    # Add the new grid to the list of grids
    all_grids.append(copy.deepcopy(grid))

print(grid)

# Find out how long a cycle is
cycle = 0
lowest_index = 0
for i in range(len(all_grids)):
    for j in range(i+1,len(all_grids)):
        if all_grids[i] == all_grids[j]:
            lowest_index = i
            cycle = j - i
            print(i, j)
            break
    if cycle != 0:
        break
print(cycle)
# Find a solution that will be the same as the one after 1 billion cycles
index = 0
for i in range(lowest_index, 10**6):
    if (10**9 - i) % cycle == 0:
        index = i-1
        break

print(index)

sum = 0
for column in all_grids[index]:
    for i in range(len(column)):
        if list(reversed(column))[i] == "O":
            sum += i + 1

print(sum)
