import copy
import os

with open("input.txt", "r") as f:
    data = f.read().splitlines()

# file = open('input.txt', 'r')
# data = file.readlines()
# file.close()


def create_grid(data):
    height = 0
    width = 0

    for line in data:
        direction = line[0]

        match direction:
            case 'R' | 'L':
                if int(line[2:]) > width:
                    width = int(line[2:])
            case 'U' | 'D':
                if int(line[2:]) > height:
                    height = int(line[2:])

    height = height * 20
    width = width * 20
    result = []
    for i in range(height + 1):
        result.append([])
        for j in range(width + 1):
            result[i].append('.')
    return result


def print_formatted_grid(grid):
    os.system('clear')
    i = 0
    for i, row in enumerate(grid):
        str_row = ""
        for j, col in enumerate(row):
            str_row += row[j] + ' '
        print(str_row)
    print('-----\n')


def update_grid():
    # Reset grid
    for row in grid:
        for i, column in enumerate(row):
            row[i] = '.'
    # Restore 's'
    grid[start_pos[0]][start_pos[1]] = 's'
    # Update 't'
    grid[t[0]][t[1]] = 'T'
    # Update 'h'
    grid[h[0]][h[1]] = 'H'
    return grid


grid = create_grid(data)
visited_grid = copy.deepcopy(grid)
# Start Position
start_pos = [len(grid) // 2, len(grid[0]) // 2]
visited_grid[start_pos[0]][start_pos[1]] = 'x'
h = [start_pos[0], start_pos[1]]
t = [start_pos[0], start_pos[1]]
grid = update_grid()


def get_movement(line):
    # [0] = Direction
    # [2:] = Distance
    return line[0], int(line[2:])


# Move head, check if tail needs to move, and set the current tail position as visited
def execute_move(direction, distance):
    i = 0
    while i < distance:
        move_head(direction)
        move_tail()
        set_tail_visited()
        i += 1
    return


# Move head one space in a certain direction
def move_head(direction):
    match direction:
        case 'R':
            h[1] += 1
        case 'L':
            h[1] -= 1
        case 'U':
            h[0] -= 1
        case 'D':
            h[0] += 1
    return


def move_tail():
    # Check if it needs to be moved
    row_diff = h[0] - t[0]
    col_diff = h[1] - t[1]

    # Move diagonally
    if (abs(row_diff) + abs(col_diff)) > 2:
        # Up and Right
        if row_diff < 0 and col_diff > 0:
            t[0] -= 1
            t[1] += 1
        # Up and Left
        elif row_diff < 0 and col_diff < 0:
            t[0] -= 1
            t[1] -= 1
        # down and right
        elif row_diff > 0 and col_diff > 0:
            t[0] += 1
            t[1] += 1
        # down and left
        elif row_diff > 0 and col_diff < 0:
            t[0] += 1
            t[1] -= 1
        return

    # Move normally
    # Up
    if row_diff < -1:
        t[0] -= 1
    # Down
    elif row_diff > 1:
        t[0] += 1
    # Right
    elif col_diff > 1:
        t[1] += 1
    # Left
    elif col_diff < -1:
        t[1] -= 1
    return


def set_tail_visited():
    visited_grid[t[0]][t[1]] = 'x'
    return


def count_no_visited_grids(grid):
    result = 0
    for row in grid:
        result += row.count('x')

    return result


for line in data:
    movement = get_movement(line)
    execute_move(movement[0], movement[1])
    update_grid()


sum_visited = count_no_visited_grids(visited_grid)
print(sum_visited)
