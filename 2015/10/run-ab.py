import re
from typing import Literal
input = '1113222113'

cycles = 50

for i in range(cycles):
    process = re.finditer(r'(\d)\1{1,}|(\d{1})', input)
    newInput = []

    for match in process:
        pos = match.span()[0]
        count = len(str(match.group()))
        newProcess = str(count) + str(match.group()[0])
        newInput.append([newProcess, pos])
    # order newInput by position
    newInput.sort(key=lambda x: x[1])
    # write newInput to input
    input = ''
    for i in newInput:
        input += i[0]


print("Length of input: " + str(len(input)))
print("Done")
