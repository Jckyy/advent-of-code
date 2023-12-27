from collections import deque


class Node:
    def __init__(self, value, left=None, right=None, up=None, down=None):
        self.value = value
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_up(self, up):
        self.up = up

    def set_down(self, down):
        self.down = down
    pass


def breadth_first_search(graph, root):
    queue = deque([root])


with open('input', 'r') as f:
    data = f.read().splitlines()


def print_map(data):
    for line in data:
        print(line)


# print_map(data)


def find_start_and_end(data):
    start = 'S'
    end = 'E'
    # end_index = [(i, data.index(end))
    #              for i, line in enumerate(data) if end in line]
    for i, line in enumerate(data):
        if start in line:
            start_index = [i, line.index(start)]
        if end in line:
            end_index = [i, line.index(end)]
    return start_index, end_index


start_idx, end_idx = find_start_and_end(data)

print(start_idx, end_idx)
