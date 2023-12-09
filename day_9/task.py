def find_last_number(numbers):
    if any(numbers):
        under_list = []
        for i in range(len(numbers) - 1):
            under_list.append(numbers[i + 1] - numbers[i])

        return find_last_number(under_list) + numbers[-1]
    else:
        return 0


def find_first_number(numbers):
    if any(numbers):
        under_list = []
        for i in range(len(numbers) - 1, 0, -1):
            under_list.insert(0, numbers[i] - numbers[i - 1])

        return numbers[0] - find_first_number(under_list)
    else:
        return 0


# Task 1

# Read input
with open("input.txt", "r") as file:
    input = file.read().splitlines()

    input = [[int(i) for i in line.split()] for line in input]

    sum = 0

    for sequence in input:
        sum += find_last_number(sequence)

    print(sum)

# Task 2

with open("input.txt", "r") as file:
    input = file.read().splitlines()

    input = [[int(i) for i in line.split()] for line in input]

    sum = 0

    for sequence in input:
        sum += find_first_number(sequence)

    print(sum)
