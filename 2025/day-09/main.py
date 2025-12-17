from common.helpers import print_array_rows
from common.helpers import read_data

# data = read_data("sample-input.txt")
# data = read_data("input.txt")
data = read_data("input2.txt")


print(data)

def create_combinations(data):
    combinations = []
    for i, point in enumerate(data):
        for j in range(i + 1, len(data)):
            p1 = [int(x) for x in data[i].split(',')]
            p2 = [int(x) for x in data[j].split(',')]
            combinations.append([p1, p2])
    return combinations

combinations = create_combinations(data)
print(combinations)
print(len(combinations))
# [[[7, 1], [11, 1]], [[7, 1], [11, 7]], [[7, 1], [9, 7]], [[7, 1], [9, 5]], [[7, 1], [2, 5]], [[7, 1], [2, 3]], [[7, 1], [7, 3]], [[11, 1], [11, 7]], [[11, 1], [9, 7]], [[11, 1], [9, 5]], [[11, 1], [2, 5]], [[11, 1], [2, 3]], [[11, 1], [7, 3]], [[11, 7], [9, 7]], [[11, 7], [9, 5]], [[11, 7], [2, 5]], [[11, 7], [2, 3]], [[11, 7], [7, 3]], [[9, 7], [9, 5]], [[9, 7], [2, 5]], [[9, 7], [2, 3]], [[9, 7], [7, 3]], [[9, 5], [2, 5]], [[9, 5], [2, 3]], [[9, 5], [7, 3]], [[2, 5], [2, 3]], [[2, 5], [7, 3]], [[2, 3], [7, 3]]]


def calculate_rectangle_area(p1, p2):
    max_x = max(p1[0], p2[0])
    min_x = min(p1[0], p2[0])

    max_y = max(p1[1], p2[1])
    min_y = min(p1[1], p2[1])

    length = max_x - min_x + 1
    height = max_y - min_y + 1

    area = length * height

    return area

test = calculate_rectangle_area([2,5],[9,7])
print(test)

max_rectangle_area = 0

for combination in combinations:
    area = calculate_rectangle_area(combination[0], combination[1])

    print(f"{combination} has an area of {area}")
    if area > max_rectangle_area:
        max_rectangle_area = area

print(f"Part one answer = {max_rectangle_area}")
# Attempt 1: 4777816465 (Correct)