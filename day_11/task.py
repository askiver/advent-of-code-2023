from tqdm import tqdm

# Task 1
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

height = len(data)
length = len(data[0])

# Find all rows with no galaxies
empty_rows = []
for i in range(height):
    if all(char == "." for char in data[i]):
        empty_rows.append(i)

# Now we can create a new grid with expanded rows
expanded_rows = []
for i in range(height):
    expanded_rows.append(data[i])
    if i in empty_rows:
        expanded_rows.append(data[i])

height = len(expanded_rows)

# Now we must find all columns with no galaxies
empty_columns = []
empty_column = True
for x in range(length):
    for y in range(height):
        if (expanded_rows[y][x] != "."):
            empty_column = False
            break
    if empty_column:
        empty_columns.append(x)
    empty_column = True

# Now we can create a new grid with expanded columns
expanded_columns = []
for i in range(height):
    row = ""
    for j in range(length):
        row += expanded_rows[i][j]
        if j in empty_columns:
            row += expanded_rows[i][j]
    expanded_columns.append(row)

length = len(expanded_columns[0])

galaxy_locations = []
for y in range(height):
    for x in range(length):
        if expanded_columns[y][x] == "#":
            galaxy_locations.append((x, y))

sum_lengths = 0
for i in range(len(galaxy_locations)):
    for j in range(i+1, len(galaxy_locations)):
        sum_lengths += abs(galaxy_locations[i][0] - galaxy_locations[j][0]) + abs(galaxy_locations[i][1] - galaxy_locations[j][1])

print(sum_lengths)


# Task 2
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

height = len(data)
length = len(data[0])

# Find all rows with no galaxies
empty_rows = []
for i in range(height):
    if all(char == "." for char in data[i]):
        empty_rows.append(i)

# Now we must find all columns with no galaxies
empty_columns = []
empty_column = True
for x in range(length):
    for y in range(height):
        if data[y][x] != ".":
            empty_column = False
            break
    if empty_column:
        empty_columns.append(x)
    empty_column = True

galaxy_locations = []
for y in range(height):
    for x in range(length):
        if data[y][x] == "#":
            galaxy_locations.append((x, y))

sum_lengths = 0
for i in range(len(galaxy_locations)):
    for j in range(i+1, len(galaxy_locations)):
        # if we cross empty galaxies, we must add 1000000 to the length of the distance
        x_range = range(galaxy_locations[i][0], galaxy_locations[j][0]+1) if galaxy_locations[i][0] < galaxy_locations[j][0] else range(galaxy_locations[j][0], galaxy_locations[i][0]+1)
        y_range = range(galaxy_locations[i][1], galaxy_locations[j][1]+1) if galaxy_locations[i][1] < galaxy_locations[j][1] else range(galaxy_locations[j][1], galaxy_locations[i][1]+1)
        for x in x_range:
            if x in empty_columns:
                sum_lengths += 10**6 - 1
        for y in y_range:
            if y in empty_rows:
                sum_lengths += 10**6 - 1

        sum_lengths += abs(galaxy_locations[i][0] - galaxy_locations[j][0]) + abs(galaxy_locations[i][1] - galaxy_locations[j][1])

print(sum_lengths)



