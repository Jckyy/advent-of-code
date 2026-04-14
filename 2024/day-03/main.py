import time
import re


def read_data(file_path):
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    return data


use_sample = False
file_path = "sample-input.txt" if use_sample else "input.txt"
# file_path = "edge-case-input.txt"
data = read_data(file_path)

### Part 1 ###
start_time = time.perf_counter()

part_1_answer = 0

regex = r"mul\((\d+),(\d+)\)"
matches = [re.findall(regex, line) for line in data]

for line in matches:
    for pair in line:
        # print(pair)
        part_1_answer += int(pair[0]) * int(pair[1])

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Part 1 answer = {part_1_answer}")
print(f"Part 1 exec time: {execution_time:.6f} seconds")
# Submission 1: 34583120 too low


### Part 2 ###
file_path = "sample-input-2.txt" if use_sample else "input.txt"
data = read_data(file_path)
start_time = time.perf_counter()
full_data = "".join(data)

part_2_answer = 0
pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
mul_enabled = True

for match in re.finditer(pattern, full_data):
    # print(match.group(0))
    instruction = match.group(0)

    if instruction == "do()":
        mul_enabled = True
    elif instruction == "don't()":
        mul_enabled = False
    else:
        # print(match.group(1), match.group(2))
        if mul_enabled:
            part_2_answer += int(match.group(1)) * int(match.group(2))

    # print(match.group(1))
    # print(match.group(2))

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Part 2 answer: {part_2_answer}")
print(f"Part 2 exec time: {execution_time:.6f} seconds")
# Submission 1: 104083373 correct
