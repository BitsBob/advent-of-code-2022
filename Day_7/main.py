#Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

cur_dir = ""
dirs = []

with open('input_data.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

curr_dir = ""
dirs = {"/home": 0}
for line in data:
    line = line.split()
    if line[0] == '$':
        if line[1] == "ls":
            pass
        else:
            if line[2] == "..":
                curr_dir = curr_dir[:curr_dir.rindex("/")]
            elif line[2] == '/':
                curr_dir = "/home"
            else:
                curr_dir = curr_dir + '/' + line[2]
                dirs[curr_dir] = 0
    else:
        if line[0] != "dir":
            tmp_pth = curr_dir
            while tmp_pth != "":
                dirs[tmp_pth] += int(line[0])
                tmp_pth = tmp_pth[:tmp_pth.rindex("/")]
print(dirs)

total = 0
for _, directory in dirs.items():
    if directory < 100000:
        total += directory

print(total)

