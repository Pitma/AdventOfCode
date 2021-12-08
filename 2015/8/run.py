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

# translate all inputs by removing leading and trailing double quotes
translatedInputs = []
for i in inputs:
    translatedInputs.append(i[1:-1])

# translate all translated inputs by removing finding and replacing all escaped characters
translatedInputs2 = []
for i in translatedInputs:
    translatedInputs2.append(i.replace('\\"', '"').replace('\\\\', '\\'))

# translate all translated inputs by finding and replacing hexadecimal escape sequences and converting them to their corresponding characters
translatedInputs3 = []
for i in translatedInputs2:
    translatedInputs3.append(
        re.sub(r'\\x[0-9a-f]{2}', lambda x: chr(int(x.group(0)[2:], 16)), i))

# count all characters in translatedInputs3
countTranslated = 0
for i in translatedInputs3:
    countTranslated += len(i)


print(countTranslated)

print(countLiteral)
print(countLiteral-countTranslated)
# print(inputs)
