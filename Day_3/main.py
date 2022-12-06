with open('/Users/Audey/Desktop/advent-of-code-2022/Day_3/input_data.txt', 'r') as f:
    lines = f.readlines()
    packs = [entry.strip() for entry in lines]

p1 = ""
p2 = ""
l1 = []
firstPacks   = []
secondPacks  = []
for pack in packs:
     p1 = pack[:len(pack)//2]
     p2 = pack[len(pack)//2:]
     firstPacks.append(p1)
     secondPacks.append(p2)

for char in p1:
     

#Checking it works:
#
#rNZNWvMZZmDDmwqNdZrWTqhJMhhgzggBhzBJBchQzzJJ
#rNZNWvMZZmDDmwqNdZrWTq
#                      hJMhhgzggBhzBJBchQzzJJ