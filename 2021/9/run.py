inputs = []
# read all values from inputTest.txt and split by ""
# an remove leading and trailing whitespace and
# an remove "\n" from each line
with open("input.txt", "r") as f:
    for line in f:
        inputs.append(line.split())

col = 100
row = len(inputs)

heights = ""
for value in inputs:
    for char in value:
        heights += char
heights = heights.replace("\n", "")


def index(i, j):
    return j + i * col


def checkNeighbours(i, j, height):

    counter = 0
    if j - 1 < 0:
        counter += 1
    elif heights[index(i, j - 1)] > height:
        counter += 1
    if j + 1 >= col:
        counter += 1
    elif heights[index(i, j + 1)] > height:
        counter += 1
    if i - 1 < 0:
        counter += 1
    elif heights[index(i - 1, j)] > height:
        counter += 1
    if i + 1 >= row:
        counter += 1
    elif heights[index(i + 1, j)] > height:
        counter += 1
    if counter >= 4:
        return True

    return False


c = 0
for i in range(row):
    for j in range(col):
        if checkNeighbours(i, j, heights[index(i, j)]):
            c = c + int(heights[index(i, j)]) + 1


print("c " + str(c))
