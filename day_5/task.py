import math


class DefaultDictWithKeyAsValue(dict):
    def __missing__(self, key):
        return key


#  task 1
# create 6 maps
maps = [[] for i in range(7)]

# Read input
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

seeds = [int(x) for x in data[0].split(" ")[1:]]

current_map = 0

for i in range(3, len(data)):
    if data[i] == '':
        current_map += 1
        continue
    elif not data[i][0].isdigit():
        continue
    else:
        ranges = [int(x) for x in data[i].split(" ")]
        maps[current_map].append(ranges)

lowest_number = math.inf

for seed in seeds:
    next_seed = seed
    for i in range(7):
        for ranges in maps[i]:
            if ranges[1] <= next_seed <= ranges[1] + ranges[2]:
                next_seed = ranges[0] + (next_seed - ranges[1])
                break
    lowest_number = min(next_seed, lowest_number)

print(lowest_number)

# Task 2

# Find the highest possible and lowest possible number
lowest_number = math.inf
highest_number = -math.inf
for i in range(0, len(seeds), 2):
    lowest_number = min(seeds[i], lowest_number)
    highest_number = max(seeds[i] + seeds[i + 1] - 1, highest_number)

# Also check the ranges
for ranges in maps:
    for num_range in ranges:
        lowest_number = min(num_range[0], num_range[1], lowest_number)
        highest_number = max(num_range[0] + num_range[2] - 1, num_range[1] + num_range[2] - 1, highest_number)


def lowest_number_task2():
    for i in range(lowest_number, highest_number + 1):
        next_number = i
        for ranges in reversed(maps):
            for num_range in ranges:
                if num_range[0] <= next_number <= num_range[0] + num_range[2] - 1:
                    next_number = num_range[1] + (next_number - num_range[0])
                    break

        for j in range(0, len(seeds), 2):
            if seeds[j] <= next_number <= seeds[j] + seeds[j + 1] - 1:
                print(i)
                return


lowest_number_task2()
