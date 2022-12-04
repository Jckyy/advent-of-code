# from functools import reduce

file = open('input.txt', 'r')
data = file.readlines()
file.close()

# ASCII
# a - z = 97 - 122
# A - Z = 65 - 90

# Item priority
# a - z = 1 - 16
# A - Z = 27 - 52

# For lowercase, subtract 96
# For uppercase, subtract 38

# chr() = unicode -> character
# ord() = character -> unicode (then we subtract)

# Part 1


# Return a list with two compartments in it in priority form
def get_rucksack_compartments(rucksack):
    priority_rucksack = convert_items_to_priority(rucksack)

    middle = int(len(priority_rucksack) / 2)
    first_compartment = priority_rucksack[: middle]
    second_compartment = priority_rucksack[middle:]

    compartments = [first_compartment, second_compartment]
    return compartments


# Convert rucksack items to priority form
def convert_items_to_priority(rucksack):
    rucksack = rucksack[: -1]
    converted_rucksack = []
    for letter in rucksack:
        if 97 <= ord(letter) <= 122:
            priority = ord(letter) - 96
            converted_rucksack.append(priority)
        else:
            priority = ord(letter) - 38
            converted_rucksack.append(priority)
    return converted_rucksack


# Find the item that is present in both compartments
# https://www.geeksforgeeks.org/python-find-common-elements-in-list-of-lists/
def find_common_item(compartments):
    # result = list(reduce(lambda i, j: i & j, (set(x) for x in compartments)))
    result = list(set.intersection(*map(set, compartments)))
    return result[0]


# Find sum of the priorities of items that appear in both compartments
sum = 0
for rucksack in data:
    compartments = get_rucksack_compartments(rucksack)
    sum += find_common_item(compartments)

print(f'Sum of item priorities that appear in both compartments: {str(sum)}')
