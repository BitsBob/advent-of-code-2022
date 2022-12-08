"""
for copying to dic
        [H]     [W] [B]            
    [D] [B]     [L] [G] [N]        
[P] [J] [T]     [M] [R] [D]        
[V] [F] [V]     [F] [Z] [B]     [C]
[Z] [V] [S]     [G] [H] [C] [Q] [R]
[W] [W] [L] [J] [B] [V] [P] [B] [Z]
[D] [S] [M] [S] [Z] [W] [J] [T] [G]
[T] [L] [Z] [R] [C] [Q] [V] [P] [H]
 1   2   3   4   5   6   7   8   9 
"""
block_dic= {
     "list_1": ["T", "D", "W", "Z", "V", "P"],
     "list_2": ["L", "S", "W", "V", "F", "J", "D"],
     "list_3": ["Z", "M", "L", "S", "V", "T", "B", "H"],
     "list_4": ["R", "S", "J"],
     "list_5": ["C", "Z", "B", "G", "F", "M", "L", "W"],
     "list_6": ["Q", "W", "V", "H", "Z", "R", "G", "B"],
     "list_7": ["V", "J", "P", "C", "B", "D", "N"],
     "list_8": ["P", "T", "B", "Q"],
     "list_9": ["H", "G", "Z", "R", "C"],
}

with open("Day_5/input_data.txt") as file:
     for line in file:
          numbers = line.split('move')[1].strip()
          number_of_blocks = int(numbers.split("from")[0].strip())
          move_from = int(line.split('from')[1].split('to')[0])
          move_to = int(line.split('from')[1].split('to')[1])
          blocks = block_dic[f"list_{move_from}"][-number_of_blocks:]
          blocks_main = blocks[::-1]
          for block in blocks_main:
               block_dic[f"list_{move_from}"].pop()
               block_dic[f"list_{move_to}"].append(block)
for list in block_dic:
     print(block_dic[list][-1])
