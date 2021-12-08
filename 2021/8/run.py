# 1 = 2 Segments
# 4 = 4 Segments
# 7 = 3 Segments
# 8 = 7 Segments
inputs = []
# read all values from inputTest.txt and split by "|"
# an remove leading and trailing whitespace and
# an remove "\n" from each line
with open("input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip().split("|"))

# remove leading and trailing whitespace from inputs
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        inputs[i][j] = inputs[i][j].strip()


# for every input[1] split in to new digit array by " "
digigits = []
for i in range(len(inputs)):
    digigits.append(inputs[i][1].split(" "))

# for each digit in the array count the number of characters
counter = 0
for i in range(len(digigits)):
    for j in range(len(digigits[i])):
        # if len of digit is 2,3,4,7 add 1 to counter
        if (
            len(digigits[i][j]) == 2
            or len(digigits[i][j]) == 3
            or len(digigits[i][j]) == 4
            or len(digigits[i][j]) == 7
        ):
            counter += 1


print("Result: " + str(counter))
# print(digigits)
