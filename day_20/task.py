# Read input
from collections import defaultdict

with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]
    senders = [line.replace(",", "").split(" ") for line in data]

print(senders)

# Part 1

receiver_dict = {}
pulse_status = {}

# First add broadcaster to receiver_dict
receiver_dict[senders[0][0]] = senders[0][2:]

# Then add all other senders to receiver_dict and pulse_status
for sender in senders[1:]:
    receiver_dict[sender[0][1:]] = sender[2:]
    if sender[0][0] == "%":
        pulse_status[sender[0][1:]] = [sender[0][0], False]
    else:
        temp_dict = {}
        for temp in senders[1:]:
            if sender[0][1:] in temp[2:]:
                temp_dict[temp[0][1:]] = False
        pulse_status[sender[0][1:]] = [sender[0][0], temp_dict]

print(receiver_dict)


def press_button(times_pressed: int):
    num_high_pulses = 0
    num_low_pulses = 0
    for i in range(times_pressed):
        num_low_pulses += 1

        queue = []

        # add broadcast receivers to queue
        for receiver in receiver_dict['broadcaster']:
            queue.append(('broadcaster', False, receiver))

        while queue:
            next_pulse = None
            # get next receiver
            receiver = queue.pop(0)
            # Count pulses
            if receiver[1]:
                num_high_pulses += 1
            else:
                num_low_pulses += 1

            # Check if rx
            if receiver[2] == 'rx' and not receiver[1]:
                print(i)
                continue

            # Check if receiver has any outputs
            if receiver[2] not in receiver_dict:
                continue

            receiver_type = pulse_status[receiver[2]][0]
            if receiver_type == "%":
                if not receiver[1]:
                    pulse_status[receiver[2]][1] = not pulse_status[receiver[2]][1]
                    next_pulse = pulse_status[receiver[2]][1]
            else:
                pulse_status[receiver[2]][1][receiver[0]] = receiver[1]
                next_pulse = not all(pulse_status[receiver[2]][1].values())

            if next_pulse is not None:
                for next_receiver in receiver_dict[receiver[2]]:
                    queue.append((receiver[2], next_pulse, next_receiver))
    return num_high_pulses, num_low_pulses

num_high_pulses, num_low_pulses = press_button(10000000000)

print(num_high_pulses)
print(num_low_pulses)
print(num_high_pulses * num_low_pulses)

