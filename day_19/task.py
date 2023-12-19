# Read file
with open("input.txt") as f:
    lines = f.readlines()

# Remove \n
lines = [line.strip() for line in lines]

# Find index of empty line
empty_line_index = lines.index("")
# Split rules and parts

rules = lines[:empty_line_index]
parts = lines[empty_line_index + 1:]

# Create a dict with all rules
rules_dict = {}
for rule in rules:
    rule = rule.split("{")
    rule_list = []
    elements = rule[1][:-1].split(",")
    for element in elements:
        element = element.split(":")
        if len(element) == 2:
            rule_list.append((element[0], element[1]))
        else:
            rule_list.append(element)
    rules_dict[rule[0]] = rule_list


def check_rule(rule, component):
    # Create a dict for all component values
    components_dict = {}
    modified_component = component[1:-1].split(",")
    for element in modified_component:
        part, value = element.split("=")
        components_dict[part] = int(value)
    component_sum = sum(components_dict.values())

    modified_rules = []

    for element in rule:
        if type(element) == tuple:
            # Check if rule needs component value
            for key in components_dict:
                if key in element[0]:
                    # Change part of rule to component value
                    modified_rule = (element[0].replace(key, str(components_dict[key])), element[1])
                    modified_rules.append(modified_rule)
        else:
            modified_rules.append(element)

    for rule in modified_rules:
        if type(rule) == tuple:
            # Check if rule is true
            if eval(rule[0]):
                if rule[1] == 'A':
                    return component_sum
                elif rule[1] == 'R':
                    return 0
                else:
                    return check_rule(rules_dict[rule[1]], component)
        else:
            if rule[0] == 'A':
                return component_sum
            elif rule[0] == 'R':
                return 0
            else:
                return check_rule(rules_dict[rule[0]], component)





acceptable_parts_sum = 0
for component in parts:
    acceptable_parts_sum += check_rule(rules_dict['in'], component)

print(acceptable_parts_sum)

# Part 2

# find all possible combinations of rules
initial_a = [i for i in range(1, 4001)]
initial_m = [i for i in range(1, 4001)]
initial_s = [i for i in range(1, 4001)]
initial_x = [i for i in range(1, 4001)]

def find_all_combinations(rules,a, m, s, x):
    # Create a dict for all component values
    components_dict = {'a': a, 'm': m, 's': s, 'x': x}

    deeper_combos = 0

    for rule in rules:
        if type(rule) == tuple:
            for key in components_dict:
                if key in rule[0]:
                    # Branch off with new ranges
                    new_list = [x for x in components_dict[key] if eval(rule[0].replace(key, str(x)))]
                    excluded_list = [x for x in components_dict[key] if not eval(rule[0].replace(key, str(x)))]
                    components_dict[key] = new_list

                    if rule[1] == 'A':
                        # return all combinations
                        combinations = 1
                        for values in components_dict.values():
                            combinations *= len(values)
                        deeper_combos += combinations
                    elif rule[1] == 'R':
                        deeper_combos += 0
                    else:
                        deeper_combos += find_all_combinations(rules_dict[rule[1]], components_dict['a'], components_dict['m'], components_dict['s'], components_dict['x'])
                    components_dict[key] = excluded_list
        else:
            if rule[0] == 'A':
                # return all combinations
                combinations = 1
                for values in components_dict.values():
                    combinations *= len(values)
                deeper_combos += combinations
            elif rule[0] == 'R':
                deeper_combos += 0
            else:
                deeper_combos += find_all_combinations(rules_dict[rule[0]], components_dict['a'], components_dict['m'], components_dict['s'], components_dict['x'])
    return deeper_combos


print(find_all_combinations(rules_dict['in'], initial_a, initial_m, initial_s, initial_x))

