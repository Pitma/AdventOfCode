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
scoreb = []
match = {"(": ")", "[": "]", "{": "}", "<": ">"}
matchReverse = {")": "(", "]": "[", "}": "{", ">": "<"}
points = {"(": 1, "[": 2, "{": 3, "<": 4}

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
    if not corrupt:
        p = 0
        for j in reversed(checkString):
            p *= 5
            p += points[j]
        scoreb.append(p)


print(sum(score))
scoreb.sort()
print(scoreb[len(scoreb) // 2])
