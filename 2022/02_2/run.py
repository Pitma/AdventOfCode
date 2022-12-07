import numpy as np
file = open("input.txt","r")
file_data = file.read()

total_score = 0
points = dict(A=1,B=2,C=3,X=1,Y=2,Z=3)
winning = dict(X="C",Y="A",Z="B",C="X",A="Y",B="Z")
draw = dict(X="A",Y="B",Z="C",A="X",B="Y",C="Z")
loose = dict(X="B",Y="C",Z="A",B="X",C="Y",A="Z")

input = file_data.split("\n")

for line in input:
    battle = line.split()
    if battle[1] == "Z":
        total_score += 6 + points.get(winning.get(battle[0]))
        print("victory")
    elif battle[1] == "Y":
        total_score += 3 + points.get(draw.get(battle[0]))
        print("draw")
    else:
        total_score += points.get(loose.get(battle[0]))
        print("loose")

print(total_score)