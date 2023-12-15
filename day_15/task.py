from collections import defaultdict
# Task 1

# Read input
with open("input.txt") as f:
    data = f.read().split(",")


def hash_algorithm(string):
    current_value = 0
    for char in string:
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


verification_number = 0

for string in data:
    verification_number += hash_algorithm(string)

print(verification_number)

# Task 2

box_dict = defaultdict(list)

for string in data:
    parts = string.split("=" if "=" in string else "-")
    instruction = parts[0]
    string_value = int(hash_algorithm(instruction))

    if "=" in string:
        focal_value = parts[1]
        for i, item in enumerate(box_dict[string_value]):
            if item.startswith(instruction + " "):
                box_dict[string_value][i] = instruction + " " + focal_value
                break
        else:
            box_dict[string_value].append(instruction + " " + focal_value)
    else:
        for i, item in enumerate(box_dict[string_value]):
            if item.startswith(instruction + " "):
                box_dict[string_value].pop(i)
                break

result = 0
for i in range(256):
    for j, value in enumerate(box_dict[i]):
        result += (i+1) * (j+1) * int(value.split(" ")[1])

print(result)


