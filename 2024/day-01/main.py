from collections import Counter
import time


def read_data(file_path):
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    return data


use_sample = True
file_path = "sample-input.txt" if use_sample else "input.txt"
data = read_data(file_path)

### Part 1 ###
start_time_1 = time.perf_counter()
left_arr = []
right_arr = []

for line in data:
    left, right = line.split()
    left_arr.append(int(left))
    right_arr.append(int(right))

left_arr.sort()
right_arr.sort()

part_1_answer = 0

# for i, _ in enumerate(left_arr):
#     similarity_score = abs(left_arr[i] - right_arr[i])
#     # print(similarity_score)
#     part_1_answer += similarity_score

for left, right in zip(left_arr, right_arr):
    diff = abs(left - right)
    part_1_answer += diff

end_time_1 = time.perf_counter()
execution_time_2 = end_time_1 - start_time_1
print(f"Part 1 answer = {part_1_answer}")
# Submission 1: 1341714 Correct
print(f"Part 2 execution time = {execution_time_2:.6f} seconds")


### Part 2 ###
start_time_2 = time.perf_counter()

# occurrences = {}
# part_2_answer = 0
#
# for left in left_arr:
#     if left not in occurrences:
#         occurrences[left] = 0
#
#         for right in right_arr:
#             if left == right:
#                 occurrences[left] += 1
#
#     similarity_score = left * occurrences[left]
#     # print(f"similarity_score for {left} = {similarity_score}")
#     part_2_answer += similarity_score
#
# print(f"part_2_answer = {part_2_answer}")
# # Submission 1: 27384707 Correct


### Part 2 Optimised ###
count = Counter(right_arr)

part_2_answer = 0

for left in left_arr:
    if left in count:
        similarity_score = left * count[left]
        part_2_answer += similarity_score

end_time_2 = time.perf_counter()
execution_time_2 = end_time_2 - start_time_2
print(f"Part 2 answer = {part_2_answer}")
print(f"Part 2 execution time = {execution_time_2:.6f} seconds")
