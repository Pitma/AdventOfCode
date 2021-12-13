cycles = 500
fishs = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]

# read inputTest.txt and return array of values split by comma
def readFile():
    with open("input.txt", "r") as f:
        return f.read().split(",")


startFishs = readFile()

# for each startFish find value in fishs array and increase second value by 1
for startFish in startFishs:
    for fish in fishs:
        if fish[0] == int(startFish):
            fish[1] = fish[1] + 1


def processFishs():
    zero = fishs[0][1]
    one = fishs[1][1]
    two = fishs[2][1]
    three = fishs[3][1]
    four = fishs[4][1]
    five = fishs[5][1]
    six = fishs[6][1]
    seven = fishs[7][1]
    eight = fishs[8][1]

    fishs[0][1] = one
    fishs[1][1] = two
    fishs[2][1] = three
    fishs[3][1] = four
    fishs[4][1] = five
    fishs[5][1] = six
    fishs[6][1] = seven + zero
    fishs[7][1] = eight
    fishs[8][1] = zero


for i in range(cycles):
    processFishs()

# sum all second values in fishs array
total = 0
for fish in fishs:
    total = total + fish[1]

print(total)
