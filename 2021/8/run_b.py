import difflib

# 1 = 2 Segments
# 2 = 6 Segments
# 3 = 5 Segments
# 4 = 4 Segments
# 5 = 5 Segments
# 6 = 6 Segments
# 7 = 3 Segments
# 8 = 7 Segments
# 9 = 6 Segments
# 0 = 6 Segments

inputs = []
# read all values from inputTest.txt and split by "|"
# an remove leading and trailing whitespace and
# an remove "\n" from each line
with open("inputTest.txt", "r") as f:
    for line in f:
        inputs.append(line.strip().split("|"))

# remove leading and trailing whitespace from inputs
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        inputs[i][j] = inputs[i][j].strip()
# 1
# 2 3
# 4
# 5 6
# 7
# for every input[1] split in to new digit array by " "
digits = []
for i in range(len(inputs)):
    digits.append(inputs[i][1].split(" "))

wire = [[1], [2], [3], [4], [5], [6], [7]]
segments = []
for i in range(len(inputs)):
    segments.append(inputs[i][0].split(" "))


def getSolvedSegment(segment):
    for i in range(len(solvedSegmentsWithDigits)):
        if solvedSegmentsWithDigits[i][1] == segment:
            x = list(solvedSegmentsWithDigits[i][0])
            print("Found: solved " + str(x))
            return x


def resolveWire(segments, solveScheme):
    x = ""
    y = ""
    # pos 1
    if solveScheme == 1:
        for i in range(len(segments)):
            if segments[i][1] == 1:
                x = segments[i][0]
            if segments[i][1] == 7:
                y = segments[i][0]
            if x and y != "":
                print(list(difflib.ndiff(x, y)))
                diff = list(difflib.ndiff(x, y))
                # find entry in diff starting with "+" and print the value
                for i in range(len(diff)):
                    if diff[i][0] == "+":
                        print("Found: 1")
                        wire[0].append(diff[i][2])
                        break
                break
    if solveScheme == 7:
        x = getSolvedSegment(4)
        x.append(wire[0][1])
        print("Found: x for 7" + str(x))
        for j in range(len(segments[0])):
            if len(segments[0][j]) == 6:
                y = segments[0][j]
                print("Found: 7")
                print("y: " + y)
            if x and y != "":
                x = sorted(x)
                y = sorted(y)
                print(list(difflib.ndiff(x, y)))
                diff = list(difflib.ndiff(x, y))
                # find entry in diff starting with "+" and print the value
                tmpCount = 0
                for i in range(len(diff)):
                    if diff[i][0] == "+":
                        tmpCount += 1

                if tmpCount == 1:
                    for i in range(len(diff)):
                        if diff[i][0] == "+":
                            print("zugewiesen")
                            wire[6].append(diff[i][2])
                            break
                else:
                    tmpCount = 0
    if solveScheme == 4:
        x = getSolvedSegment(1)
        x.append(wire[0][1])
        print(wire)
        print("Found: x for 4" + str(x))
        x.append(wire[6][1])
        print("x: " + str(x))
        for j in range(len(segments[0])):
            if len(segments[0][j]) == 5:
                y = segments[0][j]
            if x and y != "":
                x = sorted(x)
                y = sorted(y)
                print(list(difflib.ndiff(x, y)))
                diff = list(difflib.ndiff(x, y))
                # find entry in diff starting with "+" and print the value
                tmpCount = 0
                for i in range(len(diff)):
                    if diff[i][0] == "+":
                        tmpCount += 1

                if tmpCount == 1:
                    for i in range(len(diff)):
                        if diff[i][0] == "+":
                            print("zugewiesen")
                            wire[3].append(diff[i][2])
                            break
                else:
                    tmpCount = 0
    if solveScheme == 2:
        x = getSolvedSegment(1)
        print("x: " + str(x))
        x.append(wire[3][1])
        print("x: " + str(x))
        for j in range(len(segments[0])):
            if len(segments[0][j]) == 4:
                y = segments[0][j]
            if x and y != "":
                x = sorted(x)
                y = sorted(y)
                print("y: " + str(y))
                print(list(difflib.ndiff(y, y)))
                diff = list(difflib.ndiff(x, y))
                # find entry in diff starting with "+" and print the value
                tmpCount = 0
                for i in range(len(diff)):
                    if diff[i][0] == "-":
                        tmpCount += 1

                if tmpCount == 1:
                    for i in range(len(diff)):
                        if diff[i][0] == "+":
                            print("zugewiesen")
                            wire[1].append(diff[i][2])
                            break
                else:
                    tmpCount = 0


# solve for each segment corresponding digit
solvedSegmentsWithDigits = []


def solveUniqueSegments():
    for i in range(len(segments)):
        for j in range(len(segments[i])):
            if len(segments[i][j]) == 2:
                solvedSegmentsWithDigits.append([segments[i][j], 1])
            elif len(segments[i][j]) == 3:
                solvedSegmentsWithDigits.append([segments[i][j], 7])
            elif len(segments[i][j]) == 4:
                solvedSegmentsWithDigits.append([segments[i][j], 4])
            elif len(segments[i][j]) == 7:
                solvedSegmentsWithDigits.append([segments[i][j], 8])


solveUniqueSegments()
# # order solvedSegmentsWithDigits by char
# for i in range(len(solvedSegmentsWithDigits)):
#     for j in range(len(solvedSegmentsWithDigits[i])):
#         if j == 0:
#             solvedSegmentsWithDigits[i][j] = sorted(solvedSegmentsWithDigits[i][j])


resolveWire(solvedSegmentsWithDigits, 1)
resolveWire(segments[0], 7)
resolveWire(segments, 4)
# resolveWire(segments, 2)
print(wire)
print(solvedSegmentsWithDigits)

# print("Result: " + str(counter))
# print(segments)
