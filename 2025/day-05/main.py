# Import data
def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()

        # Convert string into list
        # data = [list(line) for line in lines]
    return data

# Print an array row by row
def print_array_rows(arr):
    for row in arr:
        print(row)

data = read_data("sample-input.txt")
# data = read_data("input.txt")

# Clean data
fresh_ranges = []
ingredient_ids = []
append_id = False

for line in data:
    if line == '':
        append_id = True
        continue
    if append_id:
        ingredient_ids.append(int(line))
    else:
        fresh_ranges.append([int(x) for x in line.split("-")])

# print(fresh_ranges)
# print(ingredient_ids)


# Part 1
sum_fresh_ids = 0
for id in ingredient_ids:
    for range in fresh_ranges:
        # print(id,range)
        if range[0] < id < range[1] + 1:
            sum_fresh_ids += 1
            break # so we don't double count an id that falls inside an overlapping range

print(f"Part 1 answer: {sum_fresh_ids}\n")
# 719: too high


# Part 2 using Set (didn't work. memory error)
# Only need # fresh_ranges
# fresh_ids = set()
# for current_range in fresh_ranges:
#     new_range = set(range(current_range[0], current_range[1] + 1))
#     fresh_ids.update(new_range)
#
# day_two_answer = len(fresh_ids)
# print(f"Day 2 answer: {day_two_answer}")


# Sort range by start num first
fresh_ranges.sort()
# print(fresh_ranges)
part_two_answer = 0
for i, current_range in enumerate(fresh_ranges):
    # print(i, current_range)
    # print(f"\n{i} start")

    # Handle adding last range then quit
    if i == len(fresh_ranges) - 1:
        part_two_answer += (current_range[1] - current_range[0] + 1)
        break


    print(f"Comparing {current_range} with {fresh_ranges[i + 1]}")
    # If no overlap with next range, add to answer and skip to next iteration
    if fresh_ranges[i + 1][0] > current_range[1]:
        print(f"No overlap. Adding {current_range[1] - current_range[0] + 1} to answer")
        part_two_answer += (current_range[1] - current_range[0] + 1)
        continue

    # Compare current range end with next range
    if fresh_ranges[i + 1][0] > current_range[0]:
        # replace the 2nd ranges start number with the first end
        print(f"Overlap start, replacing {fresh_ranges[i + 1][0]} with {current_range[1]}")
        fresh_ranges[i + 1][0] = current_range[0]
    # if end of 2nd range < end of 1st range, replace with the 1st range's end
    if fresh_ranges[i + 1][1] < current_range[1]:
        print(f"Overlap start, replacing {fresh_ranges[i + 1][1]} with {current_range[1]}")
        fresh_ranges[i + 1][1] = current_range[1]

print(f"Part two answer {part_two_answer}")
# 338693411431456 correct