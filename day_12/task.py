from functools import lru_cache

# Task 1
# Read input
with open("input.txt", "r") as file:
    data = file.read().splitlines()


# Create function that verifies that a combination is valid
def verify_combination(combination, groups):
    groups = list(groups)
    i = 0
    while i < len(combination):
        if combination[i] == '#':
            if not groups:
                return False
            if not all(char == '#' for char in combination[i:i + groups[0]]):
                return False
            if i + groups[0] < len(combination):
                if combination[i + groups[0]] == '#':
                    return False
            i += groups[0]
            groups.pop(0)
        else:
            i += 1
    return True


def lexico_permute_string(s):
    ''' Generate all permutations in lexicographic order of string `s`

        This algorithm, due to Narayana Pandita, is from
        https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

        To produce the next permutation in lexicographic order of sequence `a`

        1. Find the largest index j such that a[j] < a[j + 1]. If no such index exists,
        the permutation is the last permutation.
        2. Find the largest index k greater than j such that a[j] < a[k].
        3. Swap the value of a[j] with that of a[k].
        4. Reverse the sequence from a[j + 1] up to and including the final element a[n].
    '''

    a = sorted(s)
    n = len(a) - 1
    while True:
        yield ''.join(a)

        # 1. Find the largest index j such that a[j] < a[j + 1]
        for j in range(n - 1, -1, -1):
            if a[j] < a[j + 1]:
                break
        else:
            return

        # 2. Find the largest index k greater than j such that a[j] < a[k]
        v = a[j]
        for k in range(n, j, -1):
            if v < a[k]:
                break

        # 3. Swap the value of a[j] with that of a[k].
        a[j], a[k] = a[k], a[j]

        # 4. Reverse the tail of the sequence
        a[j + 1:] = a[j + 1:][::-1]


possible_instructions = 0

for row in data:
    # Split on space
    row = row.split(' ')
    instruction = row[0]
    damaged_spring_list = [int(i) for i in row[1].split(',')]
    # Find number of damaged springs already present
    num_damaged_springs = instruction.count('#')
    num_question_marks = instruction.count('?')
    new_hashtags = sum(damaged_spring_list) - num_damaged_springs
    # Find number of periods needed
    num_periods = num_question_marks - new_hashtags
    # Create string of periods and hashtags
    string = '.' * num_periods + '#' * new_hashtags
    # Find all permutations of the string
    for permutation in lexico_permute_string(string):
        # Replace question marks in instruction with permutation
        new_instruction = instruction
        for i in range(len(permutation)):
            new_instruction = new_instruction.replace('?', permutation[i], 1)
        if verify_combination(new_instruction, tuple(damaged_spring_list)):
            possible_instructions += 1
print(possible_instructions)


# Task 2
# Permutations seem to suck for this task, so I'll try dynamic programming
@lru_cache(maxsize=None)
def count(springs, nums, consecutive=False):
    nums = list(nums)

    if not springs:
        return int(not nums or (len(nums) == 1 and not nums[0]))

    if not nums:
        return int('#' not in springs)

    head, *tail = nums

    if springs[0] == '#':
        return count(springs[1:], tuple([head - 1] + tail), True) if head else 0

    if springs[0] == '.':
        if consecutive:
            return 0 if head else count(springs[1:], tuple(tail))
        else:
            return count(springs[1:], tuple(nums))

    if consecutive:
        return count(springs[1:], tuple([head - 1] + tail), True) if head else (
            count(springs[1:], tuple(tail)))
    return count(springs[1:], tuple(nums)) + count(springs[1:], tuple([head - 1] + tail), True)


total_count = 0
for row in data:
    # Split on space
    row = row.split(' ')
    instruction = row[0]
    damaged_spring_list = [int(i) for i in row[1].split(',')]
    # Number of instructions and number of damaged springs is much higher in task 2
    big_instruction = instruction
    for i in range(4):
        big_instruction += '?' + instruction
    damaged_spring_list = damaged_spring_list * 5

    total_count += count(big_instruction, tuple(damaged_spring_list))

print(total_count)
