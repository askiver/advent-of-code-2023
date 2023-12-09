from math import inf


def find_sum(input):
    print(input)
    sum = 0
    for element in input:
        # Find first digit
        for character in element:
            if character.isdigit():
                first_digit = character
                break
        # Find last digit
        for character in reversed(element):
            if character.isdigit():
                last_digit = character
                break
        sum += int(first_digit + last_digit)
    print(sum)


# Part 1
# read input from file
with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    find_sum(input)

# Part 2
# create dictionary mapping for all numbers in the input
possible_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
reversed_possible_values = possible_values[::-1]
number_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# read input from file
with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    new_input = []
    sum = 0
    # Transform input to numbers
    for index, element in enumerate(input):
        first_index = inf
        value_length = 0
        # Find first fitting number
        for number in possible_values:
            if number in element:
                if element.find(number) < first_index:
                    first_index = min(first_index, element.find(number))
                    value_length = len(number)
        # Check if value is already digit
        if element[first_index].isdigit():
            first_digit = element[first_index]
        else:
            first_digit = number_map[element[first_index:first_index + value_length]]
        # Find last fitting number
        last_index = -inf
        value_length = 0
        for number in possible_values:
            if number in element:
                if element.rfind(number) > last_index:
                    last_index = max(last_index, element.rfind(number))
                    value_length = len(number)
        # Check if value is already digit
        if element[last_index].isdigit():
            last_digit = element[last_index]
        else:
            last_digit = number_map[element[last_index:last_index + value_length]]
        sum += int(first_digit + last_digit)
    print(sum)





