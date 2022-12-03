# Find the highest total calorie count from an individual elf
file = open("input.txt", 'r')
data = file.readlines()


# print(data[15] == "\n")

sumData = []
sum = 0
for line in data:
    if line == "\n":
        sumData.append(sum)
        sum = 0
        continue
    sum += int(line)

print(max(sumData))
