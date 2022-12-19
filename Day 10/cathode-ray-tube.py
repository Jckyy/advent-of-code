with open("input", "r") as f:
    data = f.read().splitlines()


# Signal strength during cycle:
# 20, 60, 100, 140, 180, 220
# Cycle no. times V in the register


# addx V takes 2 cycles to complete
# coop takes 1 cycle to complete

# Have a list that tracks the running addv instructions
# [ [Cycles left until finish, Value], [], [], [] ]

# Start cycle
# Begin instruction
# Finish cycle
# Finish any instructions
# Loop


# Adds addx instructions to running_instructions
def execute_instruction(line):
    global cycle
    if line[:4] == 'addx':
        num = int(line[5:])
        for i in range(2):
            check_significant_cycle()
            cycle += 1
        global x_reg
        print(cycle, x_reg)
        x_reg += num
    elif line[:4] == 'noop':
        check_significant_cycle()
        cycle += 1
    return


def check_significant_cycle():
    if cycle in significant_cycles:
        significant_values.append(x_reg)
    return


def calc_signal_strengths(cycles, values):
    result = 0
    for i, x in enumerate(values):
        result += x * cycles[i]
    return result


# x starts at 1
x_reg = 1
significant_cycles = [20, 60, 100, 140, 180, 220]
significant_values = []
cycle = 1
for line in data:
    # print(running_instructions)
    execute_instruction(line)
    # print(cycle, x)
signal_strength = calc_signal_strengths(significant_cycles, significant_values)
print(signal_strength)
