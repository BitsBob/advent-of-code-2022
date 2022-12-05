with open('/Users/Audey/advent-of-code-2022/Day_1/input_data.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]
    
elf_sums = []
running_total = 0

for entry in calories:
     if entry != '':
          running_total += int(entry)
     if entry == '':
          elf_sums.append(running_total)
          running_total = 0

elf_sums.sort(reverse=True)

print(elf_sums[0])
print(elf_sums[0] + elf_sums[1] + elf_sums[2])
