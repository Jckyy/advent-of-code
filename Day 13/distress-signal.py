import ast

with open('input', 'r') as f:
    data = f.read().splitlines()


# Create a list where each index is a pair to be compared
def create_pairs(data):
    pairs = []
    pair = []
    for line in data:
        # Split packets
        if line == '':
            pairs.append(pair)
            pair = []
            continue
        pair.append(ast.literal_eval(line))
    pairs.append(pair)
    return pairs


def compare_pair(pair, result):
    left = pair[0]
    right = pair[1]
    # print(f'Comparing:\n{left}\nand\n{right}\n')
    is_converted = False

    # Exit if false
    if not result:
        return result, False

    # if mixed
    if type(left) != type(right):
        # convert int to list
        left, right = convert_pair(left, right)
        is_converted = True

    # if both are integers
    if type(left) == int and type(right) == int:
        result, keep_going = compare_ints(left, right)
        # print(f'Returning comp of {left} and {right}')
        return result, keep_going

    # if both are lists
    elif type(left) == list and type(right) == list:
        # if lists are not empty
        if len(left) != 0 and len(right) != 0:
            # Loop through the left list
            try:
                # Loop through left value
                for i, left_value in enumerate(left):
                    # recurse
                    result, keep_going = compare_pair(
                        [left_value, right[i]], result)

                    # keep_going = True when the integers are the same
                    if not keep_going:
                        return result, keep_going
                return result, False
            # If IndexError, right list is shorter than the left
            except IndexError:
                # Same as len(right) < len(left)
                if is_converted:
                    return False, False

        # if left list is longer and right list is shorter
        if len(left) > len(right):
            return not result, False
    return result, False


# Returns both values as a list
def convert_pair(left, right):
    if type(left) == int:
        return [left], right
    return left, [right]


# compare / check if left is lower
# 2nd return value is whether to keep iterating through the list or not.
def compare_ints(left_int, right_int):
    # if same, go next int
    # if lower, return true, else false
    if left_int == right_int:
        return True, True
    return left_int < right_int, False


pairs = create_pairs(data)


correct_orders = []
for i, pair in enumerate(pairs):
    # Compare one pair
    res, dick = compare_pair(pair, True)
    if res:
        print(i + 1)
        correct_orders.append(i + 1)

print(sum(correct_orders))

# print('result:::')
# print(pairs[50][0])
# print(pairs[50][1])
# print(compare_pair(pairs[50], True)[0])
