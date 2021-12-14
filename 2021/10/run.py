from collections import deque


inputs = []
# read all values from inputTest.txt and split by ""
# an remove leading and trailing whitespace and
# an remove "\n" from each line
with open("input.txt", "r") as f:
    for line in f:
        inputs.append(line)

treffer = 0

score = []
match = {"(": ")", "[": "]", "{": "}", "<": ">"}
matchReverse = {")": "(", "]": "[", "}": "{", ">": "<"}

s = {")": 3, "]": 57, "}": 1197, ">": 25137}

for line in inputs:
    corrupt = False
    checkString = deque()
    for i in line.strip():
        if i in match:
            checkString.append(i)
        elif i in match.values():
            if str(checkString.pop()) != matchReverse[i]:
                print("Corrupt: " + str(i))
                score.append(s[i])
                corrupt = True
                break


print(sum(score))
