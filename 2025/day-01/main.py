# Import data
def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    return data

# Print an array row by row
def print_array_rows(arr):
    for row in arr:
        print(row)


# data = read_data("sample-input.txt")
# data = read_data("input.txt")
data = read_data("input-2.txt")
print_array_rows(data)

# Have current_number represent the dial

# # Initialise the dial
# current_pos = 50
# # Initialise the password
# part_one_answer = 0
# part_two_answer = 0
#
# # Loop through the instructions
# # For each iteration:
# for instruction in data:
#     initial_pos = current_pos
#     # Read the first character to get the direction
#     direction = instruction[0]
#     # Read the remaining characters for the distance and convert to int
#     distance = int(instruction[1:])
#     # Add or subtract it from the current_number
#     if direction == "L":
#         current_pos -= distance
#     else:
#         current_pos += distance
#
#     # Mod the current_number by 100 to get the final dial position
#     current_pos = current_pos % 100
#
#     # Print current dial location
#     # print(current_pos)
#
#     # Increment answer if current_pos == 0
#     if current_pos == 0:
#         part_one_answer += 1
#
# print(f"Part 1 Answer: {part_one_answer}")
# print(f"Part 2 Answer: {part_two_answer}")

# Attempt 1: 6272 Too high
# Attempt 2: 5052 Too low
# Attempt 3: 4964 Too low
# Attempt 4: 5491


# Initialise the dial
current_pos = 50
# Initialise the password
part_one_answer = 0
part_two_answer = 0

# Loop through the instructions
# For each iteration:
for instruction in data:
    # Read the first character to get the direction
    direction = instruction[0]
    # Read the remaining characters for the distance and convert to int
    distance = int(instruction[1:])
    # Add or subtract it from the current_number
    if direction == "L":
        while distance > 0:
            current_pos = (current_pos - 1) % 100
            if current_pos == 0:
                part_two_answer += 1
            distance -= 1
    else:
        while distance > 0:
            current_pos = (current_pos + 1) % 100
            if current_pos == 0:
                part_two_answer += 1
            distance -= 1

    # Mod the current_number by 100 to get the final dial position
    # current_pos = current_pos % 100

    # Print current dial location
    # print(current_pos)

    # Increment answer if current_pos == 0
    if current_pos == 0:
        part_one_answer += 1

print(f"Part 1 Answer: {part_one_answer}")
print(f"Part 2 Answer: {part_two_answer}")

