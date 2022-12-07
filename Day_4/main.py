total = 0
for line in open('Day_4/input_data.txt', 'r'):
     a, b = line.split(",")
     one = [i for i in range(int(a.split('-')[0]), int(a.split('-')[1])+1)]
     two = [i for i in range(int(b.split('-')[0]), int(b.split('-')[1])+1)]
     if all(item in one for item in two) or all(item in two for item in one):
          total += 1

print(total)
