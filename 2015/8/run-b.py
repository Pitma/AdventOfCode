import re
inputs = []
# read inputs from file
with open('input.txt') as f:
    for line in f:
        inputs.append(line.strip())

# count all characters in all inputs
countLiteral = 0
for i in inputs:
    countLiteral += len(i)


# escape backslashes and double quotes in all inputs
escapedInputs = []
for i in inputs:
    escapedInputs.append(i.replace('\\', '\\\\').replace('"', '\\"'))

# add surrounding double quotes to all inputs
translatedInputs = []
for i in escapedInputs:
    translatedInputs.append('"' + i + '"')


# count all characters in translatedInputs
countTranslated = 0
for i in translatedInputs:
    countTranslated += len(i)

# print(inputs)
# print(escapedInputs)
# print(translatedInputs)


print(countLiteral)
print(countTranslated)
print(countTranslated - countLiteral)
