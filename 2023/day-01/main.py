# import regular expression
import re 

with open('input.txt', 'r') as f:
# with open('sample-input-02.txt', 'r') as f:
    data = f.read().splitlines()


# # ---------------------------------- Part 1 ---------------------------------- #
numbers_regex = '[0-9]'
line_numbers = []

for line in data:
    # find number using regex
    numbers = re.findall(numbers_regex, line)
    # join the numbers
    if len(numbers) == 2:
        line_numbers.append(int(numbers[0] + numbers[1]))
    else:
        line_numbers.append(int(numbers[0] + numbers[-1]))

def sum_array(arr):
    # sum the numbers
    sum = 0
    for i in arr:
        sum += i
    return sum


print(f'Part 1: {sum_array(line_numbers)}')


# ---------------------------------- Part 2 ---------------------------------- #
numbers_regex = r'(?:[1-9]|one|two|three|four|five|six|seven|eight|nine)'

def search_from_start(str):
    i = 0
    while i < len(str):
        if str[i].isdigit():
            return str[i]
        
        try:
            if str[i:i+3] == 'one':
                return '1'
            elif str[i:i+3] == 'two':
                return '2'
            elif str[i:i+5] == 'three':
                return '3'
            elif str[i:i+4] == 'four':
                return '4'
            elif str[i:i+4] == 'five':
                return '5'
            elif str[i:i+3] == 'six':
                return '6'
            elif str[i:i+5] == 'seven':
                return '7'
            elif str[i:i+5] == 'eight':
                return '8'
            elif str[i:i+4] == 'nine':
                return '9'
            else:
                pass
        except IndexError:
            pass
        i += 1


def search_from_end(str):
    i = len(str)
    while i >= 0:
        try:
            if str[i].isdigit():
                return str[i]
        except IndexError:
            pass
        try:
            if str[i:i+3] == 'one':
                # print (str[i:i+3])
                return '1'
            elif str[i:i+3] == 'two':
                return '2'
            elif str[i:i+5] == 'three':
                return '3'
            elif str[i:i+4] == 'four':
                return '4'
            elif str[i:i+4] == 'five':
                return '5'
            elif str[i:i+3] == 'six':
                return '6'
            elif str[i:i+5] == 'seven':
                return '7'
            elif str[i:i+5] == 'eight':
                return '8'
            elif str[i:i+4] == 'nine':
                return '9'
        except IndexError:
            pass
        i -= 1

line_numbers = []

for line in data:
    numbers = []
    numbers.append(search_from_start(line))
    numbers.append(search_from_end(line))
    # print(numbers)
    line_numbers.append(int(numbers[0] + numbers[1]))
        
# print(line_numbers)

print(f'Part 2: {sum_array(line_numbers)}')