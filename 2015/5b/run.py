inputs = []

# read inputs from file and delete newline
with open('input.txt') as f:
    for line in f:
        inputs.append(line.rstrip('\n'))

print(inputs)

# check if inputstring contains a pair of two letters that appears at least twice in the string without overlapping


def check_input(inputstring):
    #print("checkStarted1 " + inputstring)
    for i in range(len(inputstring)-1):

        hit = str(inputstring[i]) + str(inputstring[i+1])

        if inputstring.count(hit) >= 2:
            print("check1 " + inputstring)
            return True
    return False


# check if inputstring contains at least one letter which repeats with exactly one letter between them, prevent out of range error

def check_input2(inputstring):
    #print("checkStarted2 " + inputstring)
    for i in range(len(inputstring)-2):
        #print(inputstring[i] + " " + inputstring[i+1] + " " + inputstring[i+2])
        if inputstring[i] == inputstring[i+2]:
            #print("check2: " + inputstring)
            return True
    return False


# check all inputs and count all nice strings
nice_strings = 0
for i in range(0, len(inputs)):
    if check_input(inputs[i]) and check_input2(inputs[i]):
        nice_strings += 1


print(nice_strings)
