file = open('input.txt')
data = file.read()[:-1]
file.close()

# --- Part One ---

# Since I expect there to be a lot of non-unique codes, an 'early exit' solution is more time efficient


# Find first character till first start-of-packet
def find_start(data, length):
    i = 0
    while i <= len(data) - length:
        code = get_code(i, data, length)
        if is_code_unique(code):
            return i + length
        i += 1
    return 'No unique codes.'


# Return split up code at an index and desired length
def get_code(i, data, length):
    return data[i:i+length]


# 'Early exit' check for duplicate letters in code
def is_code_unique(code):
    s = set()
    for j in code:
        if j in s:
            return False
        s.add(j)
    return True


print(find_start(data, 4))

# --- Part Two ---
print(find_start(data, 14))
