def findMarkerPartOne(data):
	for i in range(0, (len(data) + 3)):
		if len(set(data[i:i+4])) == 4:
			return i + 4, data[i:i+4]
def findMarkerPartTwo(data):
	for i in range(0, (len(data) + 13)):
		if len(set(data[i:i+14])) == 14:
			return i + 14, data[i:i+14], len(data[i:i+14])
	
with open('Day_6/input_data.txt', 'r') as f:
	data = f.readline()
	print(findMarkerPartOne(data))
	print(findMarkerPartTwo(data))