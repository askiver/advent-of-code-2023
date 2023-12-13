import functools
import re

# Task 1
# First load the data
poker_hands = []
data = ""
with open("input.txt", "r") as f:
    data = f.readlines()
    # Remove newlines
    data = [line.strip() for line in data]
    for hand in data:
        poker_hands.append([hand.split(" ")[0], int(hand.split(" ")[1])])

hand_values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


# Function that find the rank of a hand based on the rules
def get_hand_rank_value(hand, joker=False):
    # If the hand contains Jokers, replace them such that the hand is as best as possible
    if joker:
        # Count the number of jokers
        joker_count = hand.count("J")
        # Remove the jokers from the hand
        hand = hand.replace("J", "")
        if hand:
            # Sort the cards in the poker hands by their count then by their value
            hand = ''.join(sorted(hand, key=lambda x: (-hand.count(x), hand_values.index(x))))
            # Add the jokers to the hand as the first cards
            hand = hand[0] * joker_count + hand
        else:
            # If the hand is empty, the hand is just the jokers
            hand = "J" * joker_count

    # Sort the cards in the poker hands by their count then by their value
    hand = ''.join(sorted(hand, key=lambda x: (-hand.count(x), hand_values.index(x))))
    # Check for 5 of a kind
    if re.search(r"(.)\1{4}", hand):
        return 6
    # Check for 4 of a kind
    elif re.search(r"(.)\1{3}", hand):
        return 5
    # Check for full house
    elif re.search(r"(.)\1{2}(.)\2{1}|^(.)\3{1}(.)\4{2}", hand):
        return 4
    # Check for 3 of a kind
    elif re.search(r"(.)\1{2}", hand):
        return 3
    # Check for 2 pairs
    elif re.search(r"(.)\1{1}(.)\2{1}|^(.)\3{1}(.)\4(.)\5{1}", hand):
        return 2
    # Check for 1 pair
    elif re.search(r"(.)\1{1}", hand):
        return 1
    # If nothing else the hand is a high card
    else:
        return 0


def compare_hands(hand_1, hand_2):
    hand_1 = hand_1[0]
    hand_2 = hand_2[0]
    # First compare the rank of the hands
    if get_hand_rank_value(hand_1) != get_hand_rank_value(hand_2):
        return get_hand_rank_value(hand_1) - get_hand_rank_value(hand_2)
    else:
        # If the rank is the same, compare the values of the cards
        for i in range(5):
            if hand_values.index(hand_1[i]) != hand_values.index(hand_2[i]):
                return hand_values.index(hand_2[i]) - hand_values.index(hand_1[i])
    # If nothing else, the hands are equal
    return 0

def compare_hands_joker(hand_1, hand_2):
    hand_1 = hand_1[0]
    hand_2 = hand_2[0]
    # First compare the rank of the hands
    if get_hand_rank_value(hand_1, True) != get_hand_rank_value(hand_2, True):
        return get_hand_rank_value(hand_1, True) - get_hand_rank_value(hand_2, True)
    else:
        # If the rank is the same, compare the values of the cards
        for i in range(5):
            if hand_values.index(hand_1[i]) != hand_values.index(hand_2[i]):
                return hand_values.index(hand_2[i]) - hand_values.index(hand_1[i])
    # If nothing else, the hands are equal
    return 0

key_func = functools.cmp_to_key(compare_hands)

sorted_hands = sorted(poker_hands, key=key_func)

sum = 0

for i in range(len(sorted_hands)):
    sum += sorted_hands[i][1] * (i + 1)

print(sum)

# Task 2
# Now knights are jokers

hand_values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

sorted_hands_joker = sorted(poker_hands, key=functools.cmp_to_key(compare_hands_joker))
sum = 0
for i in range(len(sorted_hands_joker)):
    sum += sorted_hands_joker[i][1] * (i + 1)
print(sum)





