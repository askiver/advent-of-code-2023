# Task 1
# Read input file
move_dict = {
    ("|", "top"): ([0, 1], "top"),
    ("|", "bottom"): ([0, -1], "bottom"),
    ("-", "left"): ([1, 0], "left"),
    ("-", "right"): ([-1, 0], "right"),
    ("L", "top"): ([1, 0], "left"),
    ("L", "right"): ([0, -1], "bottom"),
    ("J", "top"): ([-1, 0], "right"),
    ("J", "left"): ([0, -1], "bottom"),
    ("7", "bottom"): ([-1, 0], "right"),
    ("7", "left"): ([0, 1], "top"),
    ("F", "bottom"): ([1, 0], "left"),
    ("F", "right"): ([0, 1], "top"),
}

data = ""
with open("input.txt", "r") as file:
    data = file.read().splitlines()

# Find max length and max height of data
max_length = len(data[0])
max_height = len(data)
# First find starting position
coordinate = [0, 0]

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            coordinate[0] = x
            coordinate[1] = y
            break

next_coord = [coordinate[0] + 1, coordinate[1]]
current_orientation = "left"

loop_nodes = set()
loop_nodes.add((coordinate[0], coordinate[1]))
number_of_moves = 1

while data[next_coord[1]][next_coord[0]] != "S":
    next_move = move_dict[(data[next_coord[1]][next_coord[0]], current_orientation)]
    loop_nodes.add((next_coord[0], next_coord[1]))
    current_orientation = next_move[1]
    next_coord[0] += next_move[0][0]
    next_coord[1] += next_move[0][1]
    number_of_moves += 1

print(number_of_moves)

# Task 2
in_loop = False
enclosed_elements = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if (x,y) in loop_nodes:
            if data[y][x] == "|":
                in_loop = not in_loop
            elif data[y][x] == "L" or data[y][x] == "S":
                while True:
                    x += 1
                    if data[y][x] == "7":
                        in_loop = not in_loop
                        break
                    elif data[y][x] == "J":
                        break
            elif data[y][x] == "F":
                while True:
                    x += 1
                    if data[y][x] == "7":
                        break
                    elif data[y][x] == "J":
                        in_loop = not in_loop
                        break
        elif in_loop:
            enclosed_elements += 1


print(enclosed_elements)



