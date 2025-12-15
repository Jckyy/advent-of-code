# # Import data
# def read_data(file_path):
#     with open(file_path, 'r') as f:
#         data = f.read().splitlines()
#
#         # lines = f.read().splitlines()
#         # Convert string into list
#         # data = [list(line) for line in lines]
#     return data
#
# # Print an array row by row
# def print_array_rows(arr):
#     for row in arr:
#         print(row)
#
# data = read_data("sample-input.txt")
# data = read_data("input.txt")
from common.helpers import print_array_rows


# #---- Part 1 ----#
# data_arr = []
# data_operators = []
# # Split data into arrays without zeros
# for i, line in enumerate(data):
#     if i == len(data) - 1:
#         # print(line.split())
#         data_operators = line.split()
#         break
#     # print([int(x) for x in line.split()])
#     data_arr.append([int(x) for x in line.split()])
#
# print(data_arr) # [[123, 328, 51, 64], [45, 64, 387, 23], [6, 98, 215, 314]]
# print(data_operators) # ['*', '+', '*', '+']
#
# part_one_answer = 0
#
# i = 0
# while i < len(data_operators):
#     problem_total = 0
#     for j, line in enumerate(data_arr):
#         if data_operators[i] == "+":
#             problem_total += line[i]
#             # print(f"Adding {line[i]}")
#         elif data_operators[i] == "*":
#             if problem_total == 0:
#                 problem_total += line[i]
#             else:
#                 problem_total *= line[i]
#             # print(f"Multiplying {line[i]}")
#     print(f"This problem {i} adds {problem_total}\n")
#     part_one_answer += problem_total
#     i += 1
#
# print(part_one_answer)
# # 4722948564882 - Correct


# Part two:

# Perform Operation Function
def execute_operator_on_array(nums_arr, op_str):
    """
    :param nums_arr: Array of int
    :param op_str: Operator provided as a string
    :return: New sum after applying operator
    """
    tmp_sum = 0
    tmp_str = ""
    if op_str == "+":
        for num in nums_arr:
            tmp_sum += num
            tmp_str += str(num) + "+"
    elif op_str == "*":
        tmp_sum = 1
        for num in nums_arr:
            tmp_sum *= num
            tmp_str += str(num) + "*"
    print(tmp_str)
    return tmp_sum


# Import data
def read_data(file_path):
    with open(file_path, 'r') as f:
        # data = f.read().splitlines()

        lines = f.read().splitlines()
        # Convert string into list
        data = [list(line) for line in lines]
    return data


data = read_data("sample-input.txt")
# data = read_data("input.txt")

# Append whitespace to the end of the shorter arrays
# Find max length array
max_array_len = max(map(len, data))
# For every array, check if it is max length:
for array in data:
    if len(array) < max_array_len:
        while len(array) < max_array_len:
            array.append(" ")

# print_array_rows(data)
# ['1', '2', '3', ' ', '3', '2', '8', ' ', ' ', '5', '1', ' ', '6', '4', ' ']
# [' ', '4', '5', ' ', '6', '4', ' ', ' ', '3', '8', '7', ' ', '2', '3', ' ']
# [' ', ' ', '6', ' ', '9', '8', ' ', ' ', '2', '1', '5', ' ', '3', '1', '4']
# ['*', ' ', ' ', ' ', '+', ' ', ' ', ' ', '*', ' ', ' ', ' ', '+', ' ', ' ']

# Remove operators from the main array & remove whitespaces
# Create new array that is equal to the last list of the data
operators = [x for x in data[-1] if x.strip()]
print(operators)  # ['*', '+', '*', '+']

data.pop()
print_array_rows(data)

# Initialise variable
op_ptr = len(operators) - 1
part_two_answer = 0

# Set pointer to move from right to left
i = len(data[0]) - 1

# While the operator pointer is 0 or more:
while op_ptr >= 0:
    current_problem_nums = [] # Array to keep the current problem's numbers

    # Check if our right to left pointer is out of bounds
    while i >= 0:
        num_str = ""

        # Iterate the rows to build the current number
        for j, element in enumerate(data):
            num_str += data[j][i]
            # print(f"num_str = {num_str}")

        print(f"final num_str = {num_str}")

        try:
            # If the current column number is not empty, add it to the array of current numbers
            num_int = int(num_str)
            current_problem_nums.append(num_int)
        except ValueError: # If the current column is empty
            # Apply the operator on the array of numbers and add to answer
            problem_sum = execute_operator_on_array(current_problem_nums, operators[op_ptr])
            part_two_answer += problem_sum

            # Reset array of nums and change operator pointer
            current_problem_nums = []
            op_ptr -= 1

        i -= 1

    # Add final problem to the total and quit
    problem_sum = execute_operator_on_array(current_problem_nums, operators[op_ptr])
    part_two_answer += problem_sum
    break

print(f"part_two_answer: {part_two_answer}")
# 9581313737063 - correct