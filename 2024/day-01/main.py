def read_data(file_path):
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    return data


# data = read_data("sample-input.txt")
data = read_data("input.txt")

# print(data)

left_arr = []
right_arr = []

for line in data:
    left, right = line.split()
    left_arr.append(int(left))
    right_arr.append(int(right))


left_arr.sort()
right_arr.sort()

# print(left_arr, right_arr)

part_1_answer = 0

for i, _ in enumerate(left_arr):
    similarity_score = abs(left_arr[i] - right_arr[i])
    # print(similarity_score)
    part_1_answer += similarity_score

print(f"Part 1 answer = {part_1_answer}")
# Submission 1: 1341714 Correct
