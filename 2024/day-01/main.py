def read_data(file_path):
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    return data


# data = read_data("sample-input.txt")
data = read_data("input.txt")

### Part 1 ###
left_arr = []
right_arr = []

for line in data:
    left, right = line.split()
    left_arr.append(int(left))
    right_arr.append(int(right))

left_arr.sort()
right_arr.sort()

part_1_answer = 0

for i, _ in enumerate(left_arr):
    similarity_score = abs(left_arr[i] - right_arr[i])
    # print(similarity_score)
    part_1_answer += similarity_score

print(f"Part 1 answer = {part_1_answer}")
# Submission 1: 1341714 Correct


### Part 2 ###
occurrences = {}
part_2_answer = 0

for left in left_arr:
    if left not in occurrences:
        occurrences[left] = 0

        for right in right_arr:
            if left == right:
                occurrences[left] += 1

    similarity_score = left * occurrences[left]
    # print(f"similarity_score for {left} = {similarity_score}")
    part_2_answer += similarity_score

print(f"part_2_answer = {part_2_answer}")
# Submission 1: 27384707 Correct
