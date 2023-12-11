# Task 1
# Read input file
move_dict = {
    ("|", "top") : ([0,1], "top"),
    ("|", "bottom") : ([0,-1], "bottom"),
    ("-", "left") : ([1,0], "left"),
    ("-", "right") : ([-1,0], "right"),
    ("L", "top") : ([1,0], "left"),
    ("L", "right") : ([0,-1], "bottom"),
    ("J", "top") : ([-1,0], "right"),
    ("J", "left") : ([0,-1], "bottom"),
    ("7", "bottom") : ([-1,0], "right"),
    ("7", "left") : ([0,1], "top"),
    ("F", "bottom") : ([1,0], "left"),
    ("F", "right") : ([0,1], "top"),
}

data = ""
with open("input.txt", "r") as file:
    data = file.read().splitlines()

# Find max length and max height of data
max_length = len(data[0])
max_height = len(data)
# First find starting position
coordinate = [0,0]

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            coordinate[0] = x
            coordinate[1] = y
            break

next_coord = [coordinate[0] + 1, coordinate[1]]
current_orientation = "left"


number_of_moves = 0
while next_coord != "S":
    print(data[next_coord[1]][next_coord[0]])
    next_move = move_dict[(data[next_coord[1]][next_coord[0]], current_orientation)]
    print(next_move)
    current_orientation = next_move[1]
    next_coord[0] += next_move[0][0]
    next_coord[1] += next_move[0][1]
    number_of_moves += 1
    print(number_of_moves)
    print(next_coord)

print(number_of_moves)


