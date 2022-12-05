# A scores 1
# B scores 2
# C scores 3
# Y = Draw scores 3
# Z = Win scores 6
# X = Loss scores 0

with open('/Users/Audey/advent-of-code-2022/Day_2/input_data.txt', 'r') as f:
    lines = f.readlines()
    pairs = [entry.strip() for entry in lines]

# Part 1
totals = []
score = 0

for pair in pairs:
     score = 0



     if pair[2] == "X":
          score += 1
          if pair[0] == "A":
               score += 3
               totals.append(score)
          if pair[0] == "B":
               score += 0
               totals.append(score)
          if pair[0] == "C":
               score += 6
               totals.append(score)



     if pair[2] == "Y":
          score += 2
          if pair[0] == "A":
               score += 6
               totals.append(score)
          if pair[0] == "B":
               score += 3
               totals.append(score)
          if pair[0] == "C":
               score += 0
               totals.append(score)



     if pair[2] == "Z":
          score += 3
          if pair[0] == "A":
               score += 0
               totals.append(score)
          if pair[0] == "B":
               score += 6
               totals.append(score)
          if pair[0] == "C":
               score += 3
               totals.append(score)

final = 0
for int in totals:
     final += int

print(f"Part 1:{final}")

# Part 2
# A scores 1 ROCK
# B scores 2 PAPER
# C scores 3 SCISSORS
# Y = Draw scores 3
# Z = Win scores 6
# X = Loss scores 0

totals = []
score = 0

for pair in pairs:
     score = 0


     if pair[0] == "A":
          if pair[2] == "X":
               score += 3
               totals.append(score)
          if pair[2] == "Y":
               score += 4
               totals.append(score)
          if pair[2] == "Z":
               score += 8
               totals.append(score)



     if pair[0] == "B":
          if pair[2] == "X":
               score += 1
               totals.append(score)
          if pair[2] == "Y":
               score += 5
               totals.append(score)
          if pair[2] == "Z":
               score += 9
               totals.append(score)



     if pair[0] == "C":
          if pair[2] == "X":
               score += 2
               totals.append(score)
          if pair[2] == "Y":
               score += 6
               totals.append(score)
          if pair[2] == "Z":
               score += 7
               totals.append(score)

final = 0
for int in totals:
     final += int

print(f"Part 2: {final}")