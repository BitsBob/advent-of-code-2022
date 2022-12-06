from string import ascii_letters

# Getting data
with open('Day_3/input_data.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

totalSum = 0
for entry in data:

    half = len(entry)//2
    
    leftSide = set(entry[:half])
    rightSide = set(entry[half:])

    for value, character in enumerate(ascii_letters):
        if character in leftSide and character in rightSide:
            totalSum += value + 1

print("Answer to part 1: ", totalSum)

totalSum = 0
j = 3

for i in range(0, len(data), 3):
    entry = data[i:j]
    j += 3

    for value, character in enumerate(ascii_letters):
        if character in entry[0] and character in entry[1] and character in entry[2]:
            totalSum += value + 1

print("Answer to part 2: ", totalSum)
