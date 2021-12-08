# read inputTest.txt and return array of values split by x and delete "\n"
def readInput():
	boxes = []
	with open("input.txt") as f:
		for line in f:
			boxes.append(line.split('x'))
	return boxes

# calculate the area of the box
def calculateArea(l, w, h):
	return 2*l*w + 2*w*h + 2*h*l

# calculate the smallest side of the box
def calculateSmallestSide(l, w, h):
	return min(l*w, w*h, h*l)

# calculate the ribbon length of the box (ribbon length + bow length)
def calculateRibbonLength(l, w, h):
	ordered = sorted([int(l), int(w), int(h)])
	return 2*ordered[0] + 2*ordered[1] + l*w*h

# for each box calculate the area and the smallest side
def calculateTotalArea(boxes):
	totalArea = 0
	totalSmallestSide = 0
	totalRibbonLength = 0
	for box in boxes:
		l, w, h = box[0], box[1], box[2]
		totalArea += calculateArea(int(l), int(w), int(h))
		totalSmallestSide += calculateSmallestSide(int(l), int(w), int(h))
		totalRibbonLength += calculateRibbonLength(int(l), int(w), int(h))
	return totalArea, totalSmallestSide, totalRibbonLength




boxes = readInput()
totalArea, totalSmallestSide,totalRibbonLength = calculateTotalArea(boxes)

print(totalArea + totalSmallestSide) # answer: 1588178
print(totalRibbonLength) # answer: 3783758
