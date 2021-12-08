import re
inputsProvide = []
inputsWire = []
finalWire = []
# read inputs from file
with open('input.txt') as f:
    for line in f:
        if re.search('^\d', line) and not re.search('AND|OR|LSHIFT|RSHIFT|NOT', line):
            inputsProvide.append(
                [line.split(' -> ')[1].rstrip(), line.split(' -> ')[0]])
        elif re.search('AND|OR|LSHIFT|RSHIFT', line):
            inputsWire.append(
                [line.split(' ')[1], line.split(' ')[0], line.split(' ')[2], line.split(' ')[4].rstrip()])
        elif re.search('NOT', line):
            inputsWire.append(
                [line.split(' ')[0], line.split(' ')[1], '', line.split(' ')[3].rstrip()])


def fillVariables():
    for i in range(len(inputsProvide)):
        for j in range(len(inputsWire)):
            if inputsProvide[i][0] == inputsWire[j][1]:
                inputsWire[j][1] = inputsProvide[i][1]
            if inputsProvide[i][0] == inputsWire[j][2]:
                inputsWire[j][2] = inputsProvide[i][1]


# check if variable is a number
def checkNumber(variable):
    if re.search('^\d', str(variable)):
        print(variable)
        return True
    else:
        return False


check = True
# if all variables are filled, calculate the result
# print(inputsProvide)


def calculateResult():
    for i in range(len(inputsWire)):
        if checkNumber(inputsWire[i][1]) and (checkNumber(inputsWire[i][2]) or inputsWire[i][0] == 'NOT'):
            if inputsWire[i][0] == 'AND':
                print("AND")
                result = int(inputsWire[i][1]) & int(inputsWire[i][2])
                inputsProvide.append([inputsWire[i][3], result])
                inputsWire.pop(i)
                break
            elif inputsWire[i][0] == 'OR':
                print("OR")
                result = int(inputsWire[i][1]) | int(inputsWire[i][2])
                inputsProvide.append([inputsWire[i][3], result])
                inputsWire.pop(i)
                break
            elif inputsWire[i][0] == 'LSHIFT':
                print("LSHIFT")
                result = int(inputsWire[i][1]) << int(inputsWire[i][2])
                inputsProvide.append([inputsWire[i][3], result])
                inputsWire.pop(i)
                break
            elif inputsWire[i][0] == 'RSHIFT':
                print("RSHIFT")
                result = int(inputsWire[i][1]) >> int(inputsWire[i][2])
                inputsProvide.append([inputsWire[i][3], result])
                inputsWire.pop(i)
                break
            elif inputsWire[i][0] == 'NOT':
                print("NOT")
                result = int(65535) - ~int(inputsWire[i][1])+1
                inputsProvide.append([inputsWire[i][3], result])
                inputsWire.pop(i)
                break
            else:
                print("ERROR")
                check = False
                break
        else:
            print(inputsWire[i])
            check = False


while len(inputsWire) > 0:
    fillVariables()
    calculateResult()
    print(inputsProvide)

    # break


# print(inputsProvide)
# find result of wire a
for i in range(len(inputsProvide)):
    if inputsProvide[i][0] == 'a':
        print("RESUUUUUUULT! " + inputsProvide[i][1])
        break

print(inputsWire)

#print("WIRE " + str(inputsWire))
