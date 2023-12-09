import numpy as np
from tqdm import tqdm


def error_margin(time, distance):
    num_possibilities = 0
    for i in tqdm(range(1, time)):
        if i*(time-i) > distance:
            num_possibilities += 1
    return num_possibilities


# Task 1
# Read file
with open('input.txt', 'r') as f:
    data = f.readlines()
    # Remove newlines
    data = [x.strip() for x in data]
    # split on colon
    data = [x.split(':')[1:] for x in data]
    # Split on space
    data = [x[0].split(' ') for x in data]
    time = data[0]
    distance = data[1]
    # Remove empty strings
    time = [x for x in time if x != '']
    distance = [x for x in distance if x != '']
    # Convert to int
    time = [int(x) for x in time]
    distance = [int(x) for x in distance]
    num_possibilities = [error_margin(t,d) for t,d in zip(time, distance)]
    sum = np.prod(num_possibilities)
    print(sum)


# Task 2
# Read file
with open('input.txt', 'r') as f:
    data = f.readlines()
    # Remove newlines
    data = [x.strip() for x in data]
    # split on colon
    data = [x.split(':')[1:] for x in data]
    # Split on space
    data = [x[0].split(' ') for x in data]
    time = data[0]
    distance = data[1]
    # Remove empty strings
    time = [x for x in time if x != '']
    distance = [x for x in distance if x != '']
    # Combine elements in list
    time = int(''.join(time))
    distance = int(''.join(distance))
    num_possibilities = error_margin(time, distance)
    print(num_possibilities)

    print(time)
    print(distance)