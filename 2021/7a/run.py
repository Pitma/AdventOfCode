# read inputTest.txt and return array of values split by comma
def readFile():
    with open("input.txt", "r") as f:
        return f.read().split(",")


# get min and max values from input
def getMinMaxPositions(input):
    min = int(input[0])
    max = int(input[0])
    for i in input:
        if int(i) < min:
            min = int(i)
        if int(i) > max:
            max = int(i)
    return min, max


input = readFile()
minPos, maxPos = getMinMaxPositions(input)


# find closest position to all numbers in steps of 1
def findClosest(input, min, max):
    distance = 0
    pos = 0
    minFuel = 0
    bestPosition = 0
    for i in range(min, max + 1):
        # go through all numbers in input and add or subtract 1 to get to i

        for j in input:
            distance += abs(int(j) - i)
            pos = i
        print(distance)
        if distance < minFuel or minFuel == 0:
            minFuel = distance
            bestPosition = pos
            distance = 0
        else:
            distance = 0

    return minFuel, bestPosition


bestFuel, bestPosition = findClosest(input, minPos, maxPos)

print("min: " + str(minPos))
print("max: " + str(maxPos))
print("best fuel: " + str(bestFuel))
print("best position: " + str(bestPosition))
