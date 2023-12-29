# Import data
def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.read().splitlines()
    return data

# Print an array row by row
def print_array_rows(arr):
    for row in arr:
        print(row)