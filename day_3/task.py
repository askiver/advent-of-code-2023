# Task 1
# read the file
with open('input.txt', 'r') as f:
    lines = f.readlines()
    # Remove newlines
    lines = [line.strip() for line in lines]
    # Find the width of the engine schematic
    width = len(lines[0])
    # Find the height of the engine schematic
    height = len(lines)

    for i in range(height):
        for j in range(width):
            # Check if current value is a digit
            if lines[i][j].isdigit():
                # Check if the number is 1, 2 or 3 digits
                if j+1 < width and lines[i][j+1].isdigit():
                    if j+2 < width and lines[i][j+2].isdigit():
                        # 3 digits
                        print(lines[i][j] + lines[i][j+1] + lines[i][j+2])
                    else:
                        # 2 digits
                        print(lines[i][j] + lines[i][j+1])
                else:
                    # 1 digit
                    print(lines[i][j])

