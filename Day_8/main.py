#  How many trees are visible from outside the grid?
row_len = len(forest(0))
with open('Day_8/input_data.txt', 'r') as f:
    forest = f.readlines()
    rows = [entry.strip() for entry in forest]

for i, row in enumerate(forest):
	col = [line[i] for line in forest]
	visible_trees_horizontal = [((i, 0), row[0])]
	visible_trees_vertical = [((0, i), col[0])]
	
	for k, tree in enumerate(row):
		if tree > visible_trees_horizontal[-1][1]:
			visible_trees_horizontal.append(((i, k), tree))
