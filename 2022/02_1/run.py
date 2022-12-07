import numpy as np
file = open("input.txt","r")
file_data = file.read()

total_score = 0
points = dict(A=1,B=2,C=3,X=1,Y=2,Z=3)
element = dict(X="C",Y="A",Z="B")
draw = dict(X="A",Y="B",Z="C")

input = file_data.split("\n")

for line in input:
    battle = line.split()
    if element.get(battle[1]) == battle[0]:
        total_score += 6 + points.get(battle[1])
        print("victory")
    elif draw.get(battle[1]) == battle[0]:
        total_score += 3 + points.get(battle[1])
        print("draw")
    else:
        total_score += points.get(battle[1])
        print("loose")

print(total_score)