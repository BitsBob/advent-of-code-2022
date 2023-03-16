#Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

with open('Day_3/input_data.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

