import numpy as np

# Task 1
# Read input
with open("input.txt") as f:
    lines = f.readlines()

value_dict = {
    "#": 1,
    ".": 0,
}

all_data = []
grid = []
current_line = []
for line in lines:
    if line.strip() == "":
        all_data.append(grid)
        grid = []
        continue
    for char in line.strip():
        current_line.append(value_dict[char])
    grid.append(current_line)
    current_line = []
all_data.append(grid)


def check_reflection(grid, value=1, smudge=False):
    half = len(grid) // 2
    if smudge:
        for i in range(1, len(grid)):
            if i <= half:
                if np.sum(grid[:i] != grid[(i * 2) - 1: i - 1:-1]) == 1:
                    return i * value
            else:
                if np.sum(grid[i - 1:(i - 1) - (len(grid) - i):-1] != grid[i:len(grid)]) == 1:
                    return i * value
    else:
        for i in range(1, len(grid)):
            if i <= half:
                if np.array_equal(grid[:i], grid[(i*2)-1: i-1:-1]):
                    return i * value
            else:
                if np.array_equal(grid[i-1:(i-1) - (len(grid)-i):-1], grid[i:len(grid)]):
                    return i * value
    return 0

sum = 0

for grid in all_data:
    grid = np.array(grid)
    sum += check_reflection(grid, 100)
    grid = np.transpose(grid)
    sum += check_reflection(grid)
print(sum)

# Task 2
sum = 0
for grid in all_data:
    grid = np.array(grid)
    sum += check_reflection(grid, 100, True)
    grid = np.transpose(grid)
    sum += check_reflection(grid, 1, True)

print(sum)