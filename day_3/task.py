# Task 1
# read the file
import re

with open('input.txt', 'r') as f:
    lines = f.readlines()
    # Remove newlines
    lines = [line.strip() for line in lines]
    # Find the width of the engine schematic
    width = len(lines[0])
    # Find the height of the engine schematic
    height = len(lines)
    sum = 0

    def check_if_symbol(height,width):
        if lines[height][width] != '.' and not lines[height][width].isdigit():
            return True

    def check_if_symbol_is_adjacent(height, width, length):
        # First check over the number
        if height > 0:
            for i in range(length):
                if check_if_symbol(height-1, width+i):
                    return True
            # Check diagonals
            if width > 0:
                if check_if_symbol(height-1, width-1):
                    return True
            if width < len(lines[0])- length:
                if check_if_symbol(height-1, width+length):
                    return True
        # Check under the number
        if height < len(lines)-1:
            for i in range(length):
                if check_if_symbol(height+1, width+i):
                    return True
            # Check diagonals
            if width > 0:
                if check_if_symbol(height+1, width-1):
                    return True
            if width < len(lines[0]) -length:
                if check_if_symbol(height+1, width+length):
                    return True
        # Check left
        if width > 0:
            if check_if_symbol(height, width-1):
                return True
        # Check right
        if width < len(lines[0]) - length:
            if check_if_symbol(height, width+length):
                return True
        return False

    for line_number, line in enumerate(lines):
        for match in re.finditer(r'\b\d+\b', line):
            start_index = match.start()
            number = match.group()
            length = len(number)
            if check_if_symbol_is_adjacent(line_number, start_index, length):
                sum += int(number)

    print(sum)

# Task 2

with open('input.txt', 'r') as f:
    lines = f.readlines()
    # Remove newlines
    lines = [line.strip() for line in lines]
    # Find the width of the engine schematic
    width = len(lines[0])
    # Find the height of the engine schematic
    height = len(lines)
    sum = 0

    for height in range(1, len(lines)-1):
        for width in range(1, len(lines[0])-1):
            if lines[height][width] == '*':
                # Check if there are adjacent numbers
                adjacent_numbers = []
                # First check over the asterix
                for match in re.finditer(r'\b\d+\b', lines[height-1]):
                    start_index = match.start()
                    number = match.group()
                    length = len(number)
                    for i in range(start_index, start_index+length):
                        if i == width-1 or i == width or i == width+1:
                            adjacent_numbers.append(number)
                            break
                # Check under the asterix
                for match in re.finditer(r'\b\d+\b', lines[height+1]):
                    start_index = match.start()
                    number = match.group()
                    length = len(number)
                    for i in range(start_index, start_index+length):
                        if i == width-1 or i == width or i == width+1:
                            adjacent_numbers.append(number)
                            break
                # Check left and right
                for match in re.finditer(r'\b\d+\b', lines[height]):
                    start_index = match.start()
                    number = match.group()
                    length = len(number)
                    if start_index + length - 1 == width-1 or start_index == width+1:
                        adjacent_numbers.append(number)
                if len(adjacent_numbers) == 2:
                    sum += int(adjacent_numbers[0]) * int(adjacent_numbers[1])
    print(sum)


