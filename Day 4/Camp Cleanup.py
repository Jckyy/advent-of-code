file = open('input.txt', 'r')
data = file.readlines()
file.close()

# --- Part 1 ---

# Find how many assignment pairs have one range fully contain the other.


# Converts a line from ['1-2', '3-8'] -> [[1,2], [3,8]]
def clean_pairs(pair):
    cleaned_pair = pair[:-1].split(',')
    for i in range(len(cleaned_pair)):
        cleaned_pair[i] = cleaned_pair[i].split('-')
        for j in range(len(cleaned_pair[i])):
            cleaned_pair[i][j] = int(cleaned_pair[i][j])
    return cleaned_pair


# Checks if the intersection of two ranges has a full overlap
def check_overlap(r1, r2, part):
    overlapping_range = r1.intersection(r2)
    if part == 'part_1':
        # Is the length of the overlapping range greater or equal to any of the ranges?
        return len(overlapping_range) >= len(r1) or len(overlapping_range) >= len(r2)
    elif part == 'part_2':
        # Is there any overlap at all?
        return len(overlapping_range) > 0


cleaned_data = []
for column in data:
    cleaned_data.append(clean_pairs(column))

count = 0
for pair in cleaned_data:
    range_1 = set(range(pair[0][0], pair[0][1]+1))
    range_2 = set(range(pair[1][0], pair[1][1]+1))
    count += check_overlap(range_1, range_2, 'part_1')
print(
    f'The number of pairs that has one range fully overlapping the other: {str(count)}')

# --- Part 2 ---

# Is there any overlap at all?

count_part_2 = 0
for pair in cleaned_data:
    range_1 = set(range(pair[0][0], pair[0][1]+1))
    range_2 = set(range(pair[1][0], pair[1][1]+1))
    count_part_2 += check_overlap(range_1, range_2, 'part_2')

print(count_part_2)
