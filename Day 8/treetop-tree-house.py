import copy

file = open('input.txt', 'r')
data = file.readlines()
file.close()

# 1. Only need to check the inside trees.
# 2. For each inside tree, check each direction.


def create_grid(data):
    grid = []
    for line in data:
        tmp = []
        for i in line[:-1]:
            tmp.append(int(i))
        grid.append(tmp)
    return grid


# Create a grid of the height of trees inside.
def get_inside_trees(grid):
    inside_trees = []
    for line in grid[1:-1]:
        inside_trees.append(line[1: -1])
    return inside_trees


# Return the total number of trees you can see.
def find_visible_trees(grid, inside_trees):
    # Duplicate a list of lists.
    set_trees = copy.deepcopy(inside_trees)

    # Check rows
    check_rows(grid, inside_trees, set_trees)

    # Check columns by transposing the lists, and use the same check left an right.
    grid = list(map(list, zip(*grid)))
    inside_trees = list(map(list, zip(*inside_trees)))
    set_trees = list(map(list, zip(*set_trees)))
    check_rows(grid, inside_trees, set_trees)

    # Count the amount of trees that have been set as visible.
    visible_tree_count = 0
    for i in set_trees:
        visible_tree_count += i.count(-1)

    # Calculate the amount of trees on the outer perimeter of the grid.
    outside = ((len(grid) * 2) + (len(grid[0]) * 2)) - 4
    visible_tree_count += outside
    return visible_tree_count


def check_rows(grid, inside_trees, set_trees):
    i = 0
    for row in inside_trees:
        # Check from left
        max = grid[i+1][0]
        j = 0
        while j < len(row):
            if inside_trees[i][j] > max:
                max = inside_trees[i][j]
                if set_trees[i][j] > 0:
                    set_trees[i][j] = -1
            j += 1
        # Check from right
        max = grid[i+1][-1]
        j = len(row) - 1
        while j >= 0:
            if inside_trees[i][j] > max:
                max = inside_trees[i][j]
                if set_trees[i][j] > 0:
                    set_trees[i][j] = -1
            j -= 1
        i += 1
    return


grid = create_grid(data)
inside_trees = get_inside_trees(grid)
visible_trees = find_visible_trees(grid, inside_trees)
print(visible_trees)
