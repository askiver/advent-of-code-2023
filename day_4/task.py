import numpy as np
# Task 1
# Read file
with open('input.txt', 'r') as f:
    sum = 0
    lines = f.readlines()
    # Remove newlines
    lines = [line.strip() for line in lines]
    # Remove the start of every string
    # Do this by splitting on colon
    lines = [line.split(': ')[1] for line in lines]
    # Now separate the winning numbers and the ticket numbers
    # Separate by |
    winning_numbers = [line.split(' | ')[0] for line in lines]
    ticket_numbers = [line.split(' | ')[1] for line in lines]
    # Now separate the winning numbers into individual numbers
    # Separate by space
    winning_numbers = [line.split(' ') for line in winning_numbers]
    # Now separate the ticket numbers into individual numbers
    # Separate by space
    ticket_numbers = [line.split(' ') for line in ticket_numbers]
    # Remove the empty strings
    winning_numbers = [[number for number in line if number != ''] for line in winning_numbers]
    ticket_numbers = [[number for number in line if number != ''] for line in ticket_numbers]
    # Convert the numbers to integers
    winning_numbers = [[int(number) for number in line] for line in winning_numbers]
    ticket_numbers = [[int(number) for number in line] for line in ticket_numbers]

    for i in range(len(winning_numbers)):
        num_correct_numbers = 0
        for number in ticket_numbers[i]:
            if number in winning_numbers[i]:
                num_correct_numbers += 1
        if num_correct_numbers > 0:
            sum += pow(2, num_correct_numbers-1)
    print(winning_numbers)
    print(ticket_numbers)
    print(sum)


# Task 2
# Read file
with open('input.txt', 'r') as f:
    sum = 0
    lines = f.readlines()
    # Remove newlines
    lines = [line.strip() for line in lines]
    # Remove the start of every string
    # Do this by splitting on colon
    lines = [line.split(': ')[1] for line in lines]
    # Now separate the winning numbers and the ticket numbers
    # Separate by |
    winning_numbers = [line.split(' | ')[0] for line in lines]
    ticket_numbers = [line.split(' | ')[1] for line in lines]
    # Now separate the winning numbers into individual numbers
    # Separate by space
    winning_numbers = [line.split(' ') for line in winning_numbers]
    # Now separate the ticket numbers into individual numbers
    # Separate by space
    ticket_numbers = [line.split(' ') for line in ticket_numbers]
    # Remove the empty strings
    winning_numbers = [[number for number in line if number != ''] for line in winning_numbers]
    ticket_numbers = [[number for number in line if number != ''] for line in ticket_numbers]
    # Convert the numbers to integers
    winning_numbers = [[int(number) for number in line] for line in winning_numbers]
    ticket_numbers = [[int(number) for number in line] for line in ticket_numbers]

    ticket_count = np.ones(len(ticket_numbers))

    for i in range(len(winning_numbers)):
        num_correct_numbers = 0
        for number in ticket_numbers[i]:
            if number in winning_numbers[i]:
                num_correct_numbers += 1
        if num_correct_numbers > 0:
            for j in range(1, num_correct_numbers+1):
                if i + j < len(ticket_count):
                    ticket_count[i+j] += ticket_count[i]
    # Find the sum of all tickets in ticket_count
    print(np.sum(ticket_count))
