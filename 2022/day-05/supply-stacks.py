file = open('input.txt')
data = file.readlines()
file.close
# print(data)

STARTING_POSITIONS = data[:9]
# print(STARTING_POSITIONS)

INSTRUCTIONS = data[10:]
# print(INSTRUCTIONS)

# Re-organise the start position data with lists
# The end of the list is the top of the stack


# Split up the instructions


# Create a nested list of the stacks
def create_stacks(data):
    indexes = range(1, len(data[0]), 4)

    stacks = []

    for i in indexes:
        column = []
        start_row = 7
        while start_row >= 0:
            if data[start_row][i] == ' ':
                break
            column.append(data[start_row][i])
            start_row -= 1
        stacks.append(column)
    return stacks


stacks = create_stacks(STARTING_POSITIONS)
# print(stacks)


def get_values(instruction):
    values = [int(s) for s in instruction.split() if s.isdigit()]
    # The above line split up
    # for s in instruction.split():
    #     if s.isdigit():
    #         values.append(int(s))
    return values


# Taking in an array of values, execute an instruction on the data
def execute_move(values, stacks, part):
    # Columns use index
    amount, initial_pos, final_pos = values[0], values[1] - 1, values[2] - 1
    # Moving crates one at a time
    if part == 'part 1':
        while amount > 0:
            stacks[final_pos].append(stacks[initial_pos][-1])
            stacks[initial_pos].pop()
            amount -= 1
    # Grab multiple crates at once and move them
    elif part == 'part 2':
        tmp = []
        # Grab the last value and put it at the start. The bottom crate will be in the first index
        while amount > 0:
            tmp.insert(0, stacks[initial_pos][-1])
            stacks[initial_pos].pop()
            amount -= 1
        for i in tmp:
            stacks[final_pos].append(i)


# Return the top value of every stack.
def get_code(stacks):
    code = ''
    for i in stacks:
        if len(i) == 0:
            code += ''
            break
        code += i[-1]
        # print(i)
    return code


for move in INSTRUCTIONS:
    instruction_values = get_values(move)
    execute_move(instruction_values, stacks, 'part 1')
print(get_code(stacks))

# --- Part Two ---

# Instead of moving one crate at a time, all crates in an instruction are moved at once.

# Reset stacks to initial position
stacks.clear()
stacks = create_stacks(STARTING_POSITIONS)

for move in INSTRUCTIONS:
    instruction_values = get_values(move)
    execute_move(instruction_values, stacks, 'part 2')

print(get_code(stacks))
