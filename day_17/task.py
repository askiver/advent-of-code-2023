from collections import defaultdict
import heapq
import numpy as np
from numpy import inf

# Task 1
# Read file
with open("input.txt", "r") as file:
    data = file.read().splitlines()

# Convert each line to a list of integers
data = [list(map(int, list(line))) for line in data]

height = len(data)
width = len(data[0])

data = np.array(data)

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


def h(current_position):
    return abs(current_position[0] - width + 1) + abs(current_position[1] - height + 1)


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


# Task 2
def a_star(least, most):
    start = [(0, 0, 'right', 0), (0, 0, 'down', 0)]
    g_score = defaultdict(lambda: inf)
    f_score = defaultdict(lambda: inf)

    open_set = []
    for s in start:
        heapq.heappush(open_set, (h(s), s))
        g_score[s] = 0
        f_score[s] = h(s)

    came_from = {}

    while open_set:
        current = heapq.heappop(open_set)[1]
        x, y, current_dir, moves = current
        if x == width - 1 and y == height - 1:
            # Check that final stretch of solution is valid
            if moves < least:
                continue
            return reconstruct_path(came_from, current)

        if moves < least:
            directions = [current_dir]
        elif moves < most:
            directions = available_directions[current_dir]
        else:
            directions = available_directions[current_dir][1:]

        for d in directions:
            moves = moves + 1 if d == current_dir else 1
            neighbour = (x + direction_mapping[d][0], y + direction_mapping[d][1], d, moves)
            if neighbour[0] < 0 or neighbour[0] >= width or neighbour[1] < 0 or neighbour[1] >= height:
                continue

            tentative_gscore = g_score[current] + data[neighbour[1]][neighbour[0]]
            if tentative_gscore < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_gscore
                f_score[neighbour] = g_score[neighbour] + h(neighbour)
                if neighbour not in open_set:
                    heapq.heappush(open_set, (f_score[neighbour], neighbour))


path = a_star(0, 3)
heat_sum = 0
for p in path[1:]:
    heat_sum += data[p[1]][p[0]]
print(heat_sum)

path = a_star(4, 10)
heat_sum = 0
for p in path[1:]:
    heat_sum += data[p[1]][p[0]]
print(heat_sum)
