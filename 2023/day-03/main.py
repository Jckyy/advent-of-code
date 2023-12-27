# Import data
with open('input.txt', 'r') as f:
# with open('sample-input.txt', 'r') as f:
    data = f.read().splitlines()

# ---------------------------------- Part 1 ---------------------------------- #

# Store number
class EngineNumber:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.width = 1

        self.include = False

    # Find the width of the number
    def find_width(self, current_x, array_2d):
        i = current_x # the x offset from start
        # print("new row", array_2d[self.start_y][self.start_x])
        while True:
            try:
                is_next_valid = array_2d[self.start_y][i+1].isdigit()
                # print(is_next_valid, array_2d[self.start_y][i+1])
                if not is_next_valid:
                    break
                else: 
                    i += 1
            except IndexError:
                break
        self.width = i - self.start_x + 1 # +1 to include the last digit
        # Since we have width, read the full number
        self.read_full_num(array_2d)

    # Check if the character is a symbol an not '.'
    def match_symbol(self, char):
        if char.isdigit() or char == '.':
            return False
        return True    

    #  Check if the number is adjacent to a symbol
    def set_include(self, array_2d):
        # Check left
        current_x = self.start_x - 1
        try:
            if self.match_symbol(array_2d[self.start_y][current_x]):
                self.include = True
                return
        except IndexError:
            pass
        # Check right
        current_x = self.start_x + self.width
        try:
            if self.match_symbol(array_2d[self.start_y][current_x]):
                self.include = True
                return
        except IndexError:
            pass
        # Bottom & Top plus width
        i = -1
        top_y = self.start_y - 1
        bot_y = self.start_y + 1
        while i <= self.width:
            try:
                current_x = self.start_x + i
                if self.match_symbol(array_2d[top_y][current_x]) or self.match_symbol(array_2d[bot_y][current_x]):
                    self.include = True
                    return
                i += 1
            except IndexError:
                i += 1

    # Read the full number from the grid
    def read_full_num(self, array_2d):
        self.value = ""
        for i in range(self.width):
            self.value += array_2d[self.start_y][self.start_x + i]
    
# Store gear - Part 2
class Gear:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.adj_nums = 0
        self.numbers = []

    def check_adj(self, included_nums):
        for num in included_nums:
            # For all numbers adjacent to a symbol
            # check if coordinates are within the range of the gear
            if num.start_x - 1 <= self.x <= num.start_x + num.width and num.start_y - 1  <= self.y <= num.start_y + 1:
                self.adj_nums += 1
                self.numbers.append(num.value)



# Store grid
array_2d = []

for line in data:
    array_2d.append(line)

numbers = []
gears = []
for y, row in enumerate(array_2d):
    # print(row)
    # Iterate through row
    x = 0
    while x < len(row): # x starts at 0
        if row[x].isdigit() == False:
            # Part 2 - Store gears
            if row[x] == '*':
                gears.append(Gear(x, y))
            x += 1
            pass
        else:
            numbers.append(EngineNumber(x, y))
            numbers[-1].find_width(x, array_2d)
            x += numbers[-1].width

# Set include to true if adjacent to symbol
for num in numbers:
    num.set_include(array_2d)

# Sum all numbers
sum = 0
included_nums = []
included_nums_obj = [] # For part 2
for num in numbers:
    if num.include:
        sum += int(num.value)   
        included_nums.append(num.value)
        included_nums_obj.append(num) # For part 2

print("Part 1 Sum:", sum)

# ---------------------------------- Part 2 ---------------------------------- #

gear_ratio_sum = 0
for gear in gears:
    gear.check_adj(included_nums_obj)
    # print(gear.numbers)
    if gear.adj_nums == 2:
        gear_ratio_sum += int(gear.numbers[0]) * int(gear.numbers[1])
print("Part 2 Sum:", gear_ratio_sum)