import operator

ops = {
    "+": operator.add,
    "*": operator.mul,
    "-": operator.sub,
}



# Import data
def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()

        # lines = f.read().splitlines()
        # Convert string into list
        # data = [list(line) for line in lines]
    return data

# Print an array row by row
def print_array_rows(arr):
    for row in arr:
        print(row)

# data = read_data("sample-input.txt")
data = read_data("input.txt")

data_arr = []
data_operators = []
for i, line in enumerate(data):
    if i == len(data) - 1:
        # print(line.split())
        data_operators = line.split()
        break
    # print([int(x) for x in line.split()])
    data_arr.append([int(x) for x in line.split()])

print(data_arr)
print(data_operators)

part_one_answer = 0

i = 0
while i < len(data_operators):
    problem_total = 0
    for j, line in enumerate(data_arr):
        if data_operators[i] == "+":
            problem_total += line[i]
            print(f"Adding {line[i]}")
        elif data_operators[i] == "*":
            if problem_total == 0:
                problem_total += line[i]
            else:
                problem_total *= line[i]
            print(f"Multiplying {line[i]}")
    print(f"This problem adds {problem_total}\n")
    part_one_answer += problem_total
    i += 1

print(part_one_answer)
# 4722948564882 - Correct