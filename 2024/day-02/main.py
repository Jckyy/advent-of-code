import time


def read_data(file_path):
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    return data


use_sample = True
file_path = "sample-input.txt" if use_sample else "input.txt"
# file_path = "edge-case-input.txt"
data = read_data(file_path)

### Part 1 ###
start_time = time.perf_counter()

part_1_answer = 0

for report in data:
    vals = [int(num) for num in report.split()]
    # print(f"Vals = {vals}")

    tmp_direction = vals[1] - vals[0]
    if tmp_direction > 0:
        isIncreasing = True
    else:
        isIncreasing = False
    # print(f"isIncreasing = {isIncreasing}")

    prev = None
    isValid = True

    for i in vals:
        # print(f"Current i = {i}")
        if not prev:
            prev = i
            continue
        diff = i - prev
        # print(f"Current diff = {diff}")
        if isIncreasing and 0 < diff < 4:
            prev = i
            continue
        elif not isIncreasing and -4 < diff < 0:
            prev = i
            continue
        else:
            isValid = False
            break

    if isValid:
        part_1_answer += 1


end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Part 1 exec time: {execution_time:.6f} seconds")
print(f"Part 1 answer = {part_1_answer}")
# Submission 1 = 220 Correct

### Part 2 ###
start_time = time.perf_counter()


# Essentially part 1 code
def is_safe(levels: list) -> bool:
    is_inc = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    is_dec = all(-3 <= levels[i + 1] - levels[i] <= -1 for i in range(len(levels) - 1))
    # # Check increasing
    # is_increasing = True
    # for i in range(len(levels) - 1):
    #     diff = levels[i + 1] - levels[i]
    #     if not (1 <= diff <= 3):
    #         is_increasing = False
    #         break

    # # Check decreasing
    # is_decreasing = True
    # for i in range(len(levels) - 1):
    #     diff = levels[i + 1] - levels[i]
    #     if not (-3 <= diff <= -1):
    #         is_decreasing = False
    #         break

    # return is_increasing or is_decreasing
    return is_inc or is_dec


part_2_answer = 0


for report in data:
    vals = [int(num) for num in report.split()]

    # Check original
    if is_safe(vals):
        part_2_answer += 1
        continue

    # Check other variants
    can_be_fixed = False
    for i in range(len(vals)):
        tmp_level = vals[:i] + vals[i + 1 :]

        if is_safe(tmp_level):
            can_be_fixed = True
            break

    if can_be_fixed:
        part_2_answer += 1


end_time = time.perf_counter()
execution_time = end_time - start_time

print(part_2_answer)
print(f"Part 2 exec time: {execution_time:.6f} seconds")
# Submission 1 = 271 Incorrect too low
# Submission 2 = 373 Incorrect too high
# Submission 3 = 272 Incorrect too low
# Submission 4 = 296 Correct
