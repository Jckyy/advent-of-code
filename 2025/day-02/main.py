# Import data
def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().split(',')
    return data

# Print an array row by row
def print_array_rows(arr):
    for row in arr:
        print(row)


data = read_data("sample-input.txt")
# data = read_data("input.txt")
print_array_rows(data)

part_one_answer = 0

# For each range
for id_range in data:
    # Split the string to get the start and end num
    first_id, last_id = id_range.split("-")
    first_id = int(first_id)
    last_id = int(last_id)
    # Iterate through the range using range(start num, end num + 1). For each iteration:
    for i in range(first_id, last_id + 1):
        current_id = str(i)
        # print(current_id)

        # If length of string is odd, skip as it can't be invalid
        if len(current_id) % 2 != 0:
            continue

        first_half = current_id[:len(current_id)//2]
        second_half = current_id[len(current_id)//2:]
        # print(f"Comparing {first_half} and {second_half}")
        # Split i by 2 and compare if they are equal to each other
        if first_half == second_half:
            # If they are equal, add the number to the result
            print(f"Adding {current_id} to result")
            part_one_answer += i

print(f"Part 1 answer: {part_one_answer}")


# Part 2
# I need to be storing how many times a sequence appears
# I'm thinking sliding window with a max size of str.length / 2
# Start checking from the max sliding window length then move down

def find_day_two_invalid_ids(current_id: str):
    # Find the maximum sliding window length len(id) // 2, and set that to current_window
    window_size = len(current_id) // 2

    # while current_window > 0:
    while window_size > 0:
        idx = 0
        while current_index < len(current_id) - window_size:
            # compare window_seq_1 & window_seq_2
            seq_1 = current_id[idx:idx+window_size]
            seq_2 = current_id[idx+window_size : idx+window_size*2]

            idx=2
            1 2 3 4 5
            seq1=123
            seq2=

            # if true
            # return true
        # if false, keep going by decreasing current_window
        # current_window - 1
    return False

# TODO: Fix the way we find the max window. e.g. 9 digit numbers can have a sequence of 3