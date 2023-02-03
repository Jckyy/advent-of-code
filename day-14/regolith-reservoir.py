import os

with open('input', 'r') as f:
    data = f.read().splitlines()


# Return list of paths, that are lists of coordinates
def clean_data(data):
    result = []
    for line in data:
        split_string = line.split(' -> ')
        coords = []
        for str in split_string:
            coords.append([int(x) for x in str.split(',')])
        result.append(coords)
    return result


def print_list(arr):
    def clear(): return os.system('cls')
    clear()
    line = '   '
    for num in range(len(arr[0])):
        # line += str(num + min_w) + ' '
        line += str(num).rjust(2, ' ') + ' '
    print(line)

    for i, value in enumerate(arr):
        line = str(i).rjust(3, ' ') + ' '
        for j in value:
            line += j + '  '
        print(line)

    # x = input()


# Create 2d array with data dimensions
def create_grid(data):
    w_min, w_max, h_max = find_map_dimensions(data)
    grid = [['.' for x in range(w_min, w_max+1)] for y in range(h_max+1)]
    return grid, w_min


def find_map_dimensions(data):
    # Don't need min_h because the index starts at 0
    min_w, max_w, h = 9999, 0, 0
    for path in data:
        for coordinate in path:
            if coordinate[0] < min_w:
                min_w = coordinate[0]
            if coordinate[0] > max_w:
                max_w = coordinate[0]
            if coordinate[1] > h:
                h = coordinate[1]
    return min_w, max_w, h


def add_rocks(data, grid, w_min):
    # Mod every x value (or the 2nd index) by w_min so they get converted into the array index
    # Draw a path between all the rocks
    # If I don't enumerate path here, I can unpack the list
    # Example: for x, y in path
    for path in data:
        for j, point in enumerate(path):
            # 1. Make a current, and target coordinate
            current_pos = [point[0] % w_min, point[1]]  # x, y
            try:
                target_pos = [path[j+1][0] % w_min, path[j+1][1]]  # x, y
                # 2. While loop of if they're not equal
                while current_pos != target_pos:
                    # Set grid position to 'x'
                    # When accessing grid[][], need to flip the indexes
                    grid[current_pos[1]][current_pos[0]] = 'x'
                    # 3. Find which value is not the same
                    # Change the first index
                    if current_pos[0] != target_pos[0]:
                        # 4. If higher add 1
                        if target_pos[0] > current_pos[0]:
                            current_pos[0] += 1
                            continue
                        # 5. If lower, subtract 1
                        current_pos[0] -= 1
                    elif current_pos[1] != target_pos[1]:
                        # 4. If higher add 1
                        if target_pos[1] > current_pos[1]:
                            current_pos[1] += 1
                            continue
                        # 5. If lower, subtract 1
                        current_pos[1] -= 1
                # Fill in the last position
                grid[current_pos[1]][current_pos[0]] = 'x'
            except IndexError:
                break
    return grid


class Sand:
    def __init__(self, w_min):
        # Sand origin on initialisation
        self._pos = [500, 0]
        self._is_set = False
        self.w_min = w_min  # Can I make a permanent attribute?

    # Update _position of sand in grid
    def move(self, grid):
        # Check if set
        if self._is_set:
            print('set')
            return

        self.x = self._pos[0] % self.w_min
        self.y = self._pos[1]

        if self.x < 0:
            print('we have an issue')
            return

        # Actually move down
        if grid[self.y + 1][self.x] == '.':
            # Add to new position
            grid[self.y + 1][self.x] = 'o'
            # Remove current position (Set to air)
            grid[self.y][self.x] = '.'
            # Update y coord for self._pos
            self._pos[1] += 1

        else:
            # print('wall or sand is underneath')
            # Move down and left
            if grid[self.y + 1][self.x - 1] == '.':
                # print('move bottom left')
                # Add to new position
                grid[self.y + 1][self.x - 1] = 'o'
                # Remove from previous pos
                grid[self.y][self.x] = '.'
                # Update _pos
                self._pos[1] += 1
                self._pos[0] -= 1

            # Move down and right
            elif grid[self.y + 1][self.x + 1] == '.':
                # print('move bottom right')
                # Add to new position
                grid[self.y + 1][self.x + 1] = 'o'
                # Remove from previous pos
                grid[self.y][self.x] = '.'
                # Update _pos
                self._pos[1] += 1
                self._pos[0] += 1
            else:
                # Can't move, set the sand
                self._is_set = True
                # print_list(grid)

        # Restore origin
        grid[0][500 % self.w_min] = '+'
        return

    def get_is_set(self):
        return self._is_set

    def get_position(self):
        return self._pos[0] % self.w_min, self._pos[1]


def mark_all_unset(grid, sand_list):
    for sand in sand_list:
        try:
            if sand.get_is_set():
                continue
            pos_x, pos_y = sand.get_position()
            grid[pos_y][pos_x] = '~'
        except IndexError:
            continue
    return grid


def main():
    # Getting the grid ready...
    cleaned_data = clean_data(data)
    grid, w_min = create_grid(cleaned_data)
    grid = add_rocks(cleaned_data, grid, w_min)
    print('broke')
    sand_origin = [0, 500 % w_min]
    grid[sand_origin[0]][sand_origin[1]] = '+'
    print_list(grid)

    sand_collection = []

    # Create new sand

    i = 0
    # Keep dropping sand until break
    while True:
        try:
            sand_collection.append(Sand(w_min))
            if "o" in grid[-1]:
                print("Overflow")
                break
            for sand in sand_collection:
                if sand.get_is_set():
                    continue
                # If not set, move
                sand.move(grid)
                # print("not set")
                # print_list(grid)
            i += 1
        except IndexError:
            break

    print('finish')
    # At this point, I need to change all the non-set sand to `~`
    grid = mark_all_unset(grid, sand_collection)
    print_list(grid)

    o_count = 0
    for line in grid:
        o_count += line.count('o')
    print(o_count)
    # Part 1 has a bug where if the sand overflows to the left,
    # the count is 1 more than it is meant to be


main()

# Part 2 Differences
# Add floor
# Need a different break statement
# - Until the block underneath the source is stuck.
