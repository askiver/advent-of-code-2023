# Task 1
# Read file
with open('input.txt', 'r') as f:
    data = f.readlines()
    # Remove newlines
    data = [x.strip() for x in data]
    move_list = data[0]
    states = data[2:]
    # Transform move list into ints based on left and right
    move_list = move_list.replace('L', '0').replace('R', '1')
    # Transform moves into list of ints
    move_list = [int(x) for x in move_list]
    # Create dictionary to store states
    states_dict = {}
    for state in states:
        states_dict[state[0:3]] = [state[7:10], state[12:15]]

    current_state = 'AAA'
    current_index = 0
    number_of_moves = 0
    while current_state != 'ZZZ':
        # Get current move
        current_move = move_list[current_index]
        # Get next state
        current_state = states_dict[current_state][current_move]
        number_of_moves += 1
        # Get next index
        current_index += 1
        if current_index >= len(move_list):
            current_index = 0

    print(number_of_moves)

# Task 2
# Read file
with open('input.txt', 'r') as f:
    data = f.readlines()
    # Remove newlines
    data = [x.strip() for x in data]
    move_list = data[0]
    states = data[2:]
    # Transform move list into ints based on left and right
    move_list = move_list.replace('L', '0').replace('R', '1')
    # Transform moves into list of ints
    move_list = [int(x) for x in move_list]
    # Create dictionary to store states
    states_dict = {}
    for state in states:
        states_dict[state[0:3]] = [state[7:10], state[12:15]]

    # Find all states that end with A
    current_states = []
    for state in states_dict:
        if state[2] == 'A':
            current_states.append(state)

    loop_lengths = []

    for state in current_states:
        current_state = state

        print(current_states)
        current_index = 0
        number_of_moves = 0

        while True:
            # Get current move
            current_move = move_list[current_index]
            # Get next state
            current_state = states_dict[current_state][current_move]
            number_of_moves += 1
            # Get next index
            current_index += 1
            if current_index >= len(move_list):
                current_index = 0
            # Check if all states end with Z
            if current_state[2] == 'Z':
                loop_lengths.append(number_of_moves)
                break

    print(loop_lengths)

    print(number_of_moves)