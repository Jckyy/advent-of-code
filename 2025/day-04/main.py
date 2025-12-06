# Import data
def read_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

        # Convert string into list
        data = [list(line) for line in lines]
    return data

# Print an array row by row
def print_array_rows(arr):
    for row in arr:
        print(row)

# data = read_data("sample-input.txt")
data = read_data("input.txt")
# print_array_rows(data)

part_one_answer = 0

# I want to make a function to check the adjacent positions

# It will take an x,y co-ordinate (row, col)
# adjacent_rolls = 0
# i should be able to just do 8 checks with edge handling for:

def check_adjacent_positions(row, col, len_row, len_col) -> int:
    adjacent_rolls = 0

    # Row above current
    if row > 0:
        # top left
        if col > 0:
            if data[row - 1][col - 1] in ["@", "x"]:
                adjacent_rolls += 1

        # top middle. will always have a top middle
        if data[row - 1][col] in ["@", "x"]:
            adjacent_rolls += 1

        # top right
        if col < len_col - 1:
            if data[row - 1][col + 1] in ["@", "x"]:
                adjacent_rolls += 1


    # Current row
    # left
    if col > 0:
        if data[row][col - 1] in ["@", "x"]:
            adjacent_rolls += 1
    # right
    if col < len_col - 1:
        if data[row][col + 1] in ["@", "x"]:
            adjacent_rolls += 1

    # Row below current
    if row < len_row - 1:
        # bottom left
        if col > 0:
            if data[row + 1][col - 1] in ["@", "x"]:
                adjacent_rolls += 1

        # bottom middle
        if data[row + 1][col] in ["@", "x"]:
            adjacent_rolls += 1

        # bottom right
        # if row == len(rows) - 1 and col == len(cols) - 1, skip
        if col < len_col - 1:
            if data[row + 1][col + 1] in ["@", "x"]:
                adjacent_rolls += 1

    # print(f"Adjacent rolls for {row}, {col}: {adjacent_rolls}")
    return adjacent_rolls

def remove_x(data):
    for row, row_list in enumerate(data):
        for col, value in enumerate(row_list):
            if value == "x":
                data[row][col] = "."
    return data

while True:
    rolls_removed = 0

    for row, cols in enumerate(data):
        # print(f"####Row {row}####")
        for col, _ in enumerate(cols):
            if data[row][col] != "@":
                continue

            adjacent_rolls = check_adjacent_positions(row, col, len(data), len(cols))
            if adjacent_rolls < 4:
                # print(f"{row}, {col} is a valid position")
                part_one_answer += 1
                rolls_removed += 1
                data[row][col] = "x"

    data = remove_x(data)

    if rolls_removed < 1:
        break



# print_array_rows(data)
print(f"Part one answer: {part_one_answer}")


# For part 2, i think the answer was given to us. We just mark a cell to be removed, then remove it later
    # Legend:
        # @ = non-changed toilet roll
        # . = no toilet roll
        # x = toilet roll to be removed
# I think a hard part is figuring out the loop to when to stop checking.
    # I need to search the data after checking all positions, and see if the amount to be removed is more than 0
    # Definitely sounds like recursion