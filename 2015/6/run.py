import math
inputs = []
lights = []
lightsCommands = []
# read inputs from file and delete newline
with open('input.txt') as f:
    for line in f:
        inputs.append(line.rstrip('\n'))


# print(inputs)


def prepareLightCommands():
    for line in inputs:
        tmp = []
        if line.startswith('turn on'):
            tmp.append(line.split(' '))
            lightsCommands.append(
                [1, tmp[0][2].split(','), tmp[0][4].split(',')])
        elif line.startswith('turn off'):
            tmp.append(line.split(' '))
            lightsCommands.append(
                [-1, tmp[0][2].split(','), tmp[0][4].split(',')])
        elif line.startswith('toggle'):
            tmp.append(line.split(' '))
            lightsCommands.append(
                [0, tmp[0][1].split(','), tmp[0][3].split(',')])
    for i in range(1000):
        lights.append([-1] * 1000)

# go through all commands and change the lights


def changeLights():
    for command in lightsCommands:
        if command[0] == 1:
            for x in range(int(command[1][0]), int(command[2][0]) + 1):
                for y in range(int(command[1][1]), int(command[2][1]) + 1):
                    lights[x][y] = 1
        elif command[0] == -1:
            for x in range(int(command[1][0]), int(command[2][0]) + 1):
                for y in range(int(command[1][1]), int(command[2][1]) + 1):
                    lights[x][y] = -1
        elif command[0] == 0:
            for x in range(int(command[1][0]), int(command[2][0]) + 1):
                for y in range(int(command[1][1]), int(command[2][1]) + 1):
                    lights[x][y] = lights[x][y] * -1


prepareLightCommands()
# print((lights))
changeLights()
# count the lights that are on
count = 0
for i in range(1000):
    for j in range(1000):
        if lights[i][j] == 1:
            count += 1
print(count)

# def get_distance(x1, y1, x2, y2):
# return (abs(x1 - x2)+1) * (abs(y1 - y2)+1)
