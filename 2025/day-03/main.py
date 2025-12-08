# Import data
def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    return data

# Print an array row by row
def print_array_rows(arr):
    for row in arr:
        print(row)



data = read_data("sample-input.txt")
data = read_data("input.txt")
# Initialise result
part_one_result = 0
# For each bank:
for bank in data:
    # Set pointer 1
    i = 0
    # Set pointer 2
    j = i + 1
    # Initialise current max to first two digits
    current_max = int(bank[i] + bank[j])
    # Start loop for pointer 1
    while i < len(bank) - 1:
        # Reset pointer 2
        j = i + 1
        # Start loop for pointer 2
        while j < len(bank):
            # Check if current number is higher than the current max
            tmp = int(bank[i] + bank[j])
            print(f"tmp is {tmp}")
            if tmp > current_max:
                current_max = tmp
                print(f"Current max is now {current_max}")
            j += 1
        i += 1
    part_one_result += current_max

print(f"Part 1 Result = {part_one_result}")