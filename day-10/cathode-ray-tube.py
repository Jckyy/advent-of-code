with open("input", "r") as f:
    data = f.read().splitlines()


# addx V takes 2 cycles to complete
# coop takes 1 cycle to complete


# Run the things that need to happen every cycle.
def execute_instruction(line):
    global cycle
    if line[:4] == 'addx':
        num = int(line[5:])
        for i in range(2):
            check_significant_cycle()
            update_display()
            cycle += 1
        global x_reg
        x_reg += num
    elif line[:4] == 'noop':
        check_significant_cycle()
        update_display()
        cycle += 1
    return


# See if the current cycle is a multiple of 40
def check_significant_cycle():
    if cycle in significant_cycles:
        significant_values.append(x_reg)
    tmp_cycle = cycle - 1
    if tmp_cycle % 40 == 0:
        global current_row
        current_row += 1
    return


def calc_signal_strengths(cycles, values):
    result = 0
    for i, x in enumerate(values):
        result += x * cycles[i]
    return result


# --- Part Two ---
def make_display():
    result = []
    for i in enumerate(range(6)):
        result.append([])
    for i, row in enumerate(result):
        for j in range(40):
            row.append('.')

    return result


def print_display(display):
    for row in display:
        print(row)


def update_display():
    if x_reg - 1 <= cycle - 1 <= x_reg + 1:
        # if cycle - 1 <= x_reg - 1 <= cycle + 1:
        # print('drawn cell')
        display[current_row][cycle-1] = '#'


# x starts at 1
x_reg = 1
current_row = 0
# Instead of this, I could've used x % 40 (except the first value)
significant_cycles = [20, 60, 100, 140, 180, 220]
significant_values = []
cycle = 1
display = make_display()
for line in data:
    execute_instruction(line)
    print(cycle, current_row, x_reg)


signal_strength = calc_signal_strengths(significant_cycles, significant_values)
print(signal_strength)
print_display(display)


# a = 5
# b = 6
# if b - 1 <= a <= b + 1:
#     print('true')
# else:
#     print('false')
