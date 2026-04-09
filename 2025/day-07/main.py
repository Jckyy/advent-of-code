from common.helpers import read_data, print_array_rows


# Have a Tachyon beam class that has:
    # fields:
        # start_pos
        # length
        # is_split
    # methods:
        # extend beam

# But how do I handle the split as you need to know:
    # if there are any overlaps and not make 2 of the same tachyon beams
        # this will need to be done outside the class

data = read_data("sample-input.txt")
# print_array_rows(data)

class TachyonBeam:
    def __init__(self, row: int, col: int):
        self.start_col = col
        self.start_row = row
        self.length = 0
        self.is_split = False

    def extend_beam(self):
        # Checks for extending beam will be done outside the class
        self.length += 1
        return

    def get_start_pos(self) -> tuple[int, int]:
        return self.start_row, self.start_col

    def get_end_pos(self) -> list[int]:
        """
        :return: Returns a list as get_next_pos needs to change the end_pos
        """
        return [self.start_row + self.length, self.start_col]

    def get_next_pos(self) -> tuple[int, int]:
        _next_pos = self.get_end_pos()
        return _next_pos[0] + 1, _next_pos[1]

    def split(self) -> list[tuple[int, int]]:
        self.is_split = True
        # Return the next two potential co-ordinates
        end_pos = self.get_end_pos()
        start_1 = (end_pos[0] + 1, end_pos[1] - 1)
        start_2 = (end_pos[0] + 1, end_pos[1] + 1)

        return [start_1, start_2]


# Split strings into arrays
for i, line in enumerate(data):
    print(list(line))
    data[i] = list(line)
# Access data as data[y][x] AKA data[row][col]

# Max iterations is len(data) - 1
MAX_ITERATIONS = len(data) - 1
split_beams = []

# Create the first beam by finding the "S"
unsplit_beams_list = [TachyonBeam(0, data[0].index("S"))]
print(unsplit_beams_list)

visited_start_positions = {unsplit_beams_list[0].get_start_pos()}
print(visited_start_positions)

part_one_answer = 0
# Go through the iterations
# I might have 2 lists to identify which ones are split so i don't need to check every beam every list
i = 1
while i < MAX_ITERATIONS:
    print(f"####Starting row {i}####")
    # Set a current_batch of beams
    current_batch = unsplit_beams_list[:]
    # For every beam:
    for beam_idx, beam in enumerate(current_batch):
        # Check if the next block for every beam if it's a '.' or '^'
        next_pos = beam.get_next_pos()
        print(f"Next pos for {beam} is {next_pos}")

        if data[next_pos[0]][next_pos[1]] == '.':
            print("Extending beam")
            beam.extend_beam()
            # TODO: Update grid to replace . with |
        elif data[next_pos[0]][next_pos[1]] == '^':
            print("Splitting beam")
            part_one_answer += 1
            split_1, split_2 = beam.split()
            # move beam to split_beams list
            split_beams.append(beam)
            # remove beam from unsplit_beams_list
            unsplit_beams_list.pop(beam_idx)
            # if first start not in unsplit_beams_list
            if split_1 not in visited_start_positions:
                print(f"Creating new beam at {split_1}")
                unsplit_beams_list.append(TachyonBeam(split_1[0], split_1[1]))
                visited_start_positions.add(unsplit_beams_list[-1].get_start_pos())
            # if second start not in unsplit_beams_list
            if split_2 not in visited_start_positions:
                print(f"Creating new beam at {split_2}")
                unsplit_beams_list.append(TachyonBeam(split_2[0], split_2[1]))
                visited_start_positions.add(unsplit_beams_list[-1].get_start_pos())
            print(f"Number of unsplit beams = {len(unsplit_beams_list)}")
    i += 1

print(len(split_beams))
print(part_one_answer)