import heapq

# Part 1
# Find the highest total calorie count from an individual elf

# Split data on '\n' and sum each segment.


def CreateCalorieList(data):
    sumData = []
    sum = 0
    for line in data:
        # print(data[15] == "\n")
        if line == "\n":
            sumData.append(sum)
            sum = 0
            continue
        sum += int(line)
    return sumData


file = open("input.txt", 'r')
data = file.readlines()
file.close()

sumData = CreateCalorieList(data)

print("Max calories: " + str(max(sumData)))


# Part 2
# How many total calories are the top 3 elves carrying?

# Return sum of a lit
def SumList(list):
    sum = 0
    for i in list:
        sum += i
    return sum


topCalories = heapq.nlargest(3, sumData)
print('Sum calories of top 3 elves: ' + str(SumList(topCalories)))
