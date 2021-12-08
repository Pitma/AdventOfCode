import difflib

inputs = []
# read all values from inputTest.txt and split by "|"
# an remove leading and trailing whitespace and
# an remove "\n" from each line

with open('inputTest.txt') as f:
    for line in f:
        inputs.append(line.strip().split("|"))

# remove leading and trailing whitespace from inputs
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        inputs[i][j] = inputs[i][j].strip()

# for every input[1] split in to new digit array by " "
digits = []
for i in range(len(inputs)):
    digits.append(inputs[i][1].split(" "))

# generate wiring examples per input
wiring = [len(inputs)-1]
for i in range(len(inputs)):
    tmpWiring = inputs[i][0].split("|")
    wiring[i] = tmpWiring[0].split(" ")

# [top, rtop,rbottom, ltop, lbottom, bottom, middle]
arrSeq = [[1, 1, 1, 1, 1, 1, 0],   # -> arrSeq[0] displays 0
          [0, 1, 1, 0, 0, 0, 0],   # -> arrSeq[1] displays 1
          [1, 1, 0, 1, 1, 0, 1],   # -> arrSeq[2] displays 2
          [1, 1, 1, 1, 0, 0, 1],   # -> arrSeq[3] displays 3
          [0, 1, 1, 0, 0, 1, 1],   # -> arrSeq[4] displays 4
          [1, 0, 1, 1, 0, 1, 1],   # -> arrSeq[5] displays 5
          [1, 0, 1, 1, 1, 1, 1],   # -> arrSeq[6] displays 6
          [1, 1, 1, 0, 0, 0, 0],   # -> arrSeq[7] displays 7
          [1, 1, 1, 1, 1, 1, 1],   # -> arrSeq[8] displays 8
          [1, 1, 1, 1, 0, 1, 1]]  # -> arrSeq[9] displays 9

wiringArrSeq = []
for i in range(len(inputs)):
    wiringArrSeq.append(arrSeq)

# 1 = 2 Segments -> unique
# 2 = 6 Segments
# 3 = 5 Segments
# 4 = 4 Segments -> unique
# 5 = 5 Segments
# 6 = 6 Segments
# 7 = 3 Segments -> unique
# 8 = 7 Segments -> unique
# 9 = 6 Segments
# 0 = 6 Segments

#
# def solveUniqueSegments(sequence, wiring):
#     for i in range(len(segments)):
#         for j in range(len(segments[i])):
#             if len(segments[i][j]) == 2:
#                 solvedSegmentsWithDigits.append([segments[i][j], 1])
#             elif len(segments[i][j]) == 3:
#                 solvedSegmentsWithDigits.append([segments[i][j], 7])
#             elif len(segments[i][j]) == 4:
#                 solvedSegmentsWithDigits.append([segments[i][j], 4])
#             elif len(segments[i][j]) == 7:
#                 solvedSegmentsWithDigits.append([segments[i][j], 8])


print(digits)
print(wiring)
print(wiringArrSeq)
