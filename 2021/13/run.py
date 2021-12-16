from collections import defaultdict, deque

file = "input.txt"


input = []
commands = []


# load file and build graph from file "value"-"connects to"
def load_graph(file):
    with open(file) as f:
        for line in f:
            line = line.strip()
            # if line contains "-"
            if "," in line:
                value, connects_to = line.strip().split(",")
                input.append([int(value), int(connects_to)])
            elif "=" in line:
                direction, fold = line.strip().split("=")
                commands.append([direction[-1], int(fold)])


load_graph(file)

width = max(input, key=lambda x: x[0])[0]
heigth = max(input, key=lambda x: x[1])[1]

matrix = [[0 for x in range(width + 1)] for y in range(heigth + 1)]

for i in range(len(input)):
    matrix[input[i][1]][input[i][0]] = 1

# count all 1s in matrix
def count_ones(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                count += 1
    return count


def fold_matrix(matrix, command, value):
    if command == "y":
        for i in range(len(matrix) - value):
            for j in range(len(matrix[i])):
                if value + i <= len(matrix) and value - i >= 0:
                    if matrix[value + i][j] == 1:
                        matrix[value - i][j] = 1
                        matrix[value + i][j] = "y"
    if command == "x":
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - value):
                if value + j <= len(matrix[i]) and value - j >= 0:
                    if matrix[i][value + j] == 1:
                        matrix[i][value - j] = 1
                        matrix[i][value + j] = "x"

    return matrix


# delete rows with at least one y
# delete columns with at least one x
def delete_rows_and_columns(matrix, command, value):
    if command == "y":
        n = len(matrix) - value
        del matrix[-n:]
    if command == "x":
        n = len(matrix[0]) - value
        for i in range(len(matrix)):
            del matrix[i][-n:]
    return matrix


# replace all 0 with "."
def replace_zeros(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][j] = "."
    return matrix


# print matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


print("---")
for command in commands:
    matrix = fold_matrix(matrix, command[0], command[1])
    matrix = delete_rows_and_columns(matrix, command[0], command[1])
print("---")
matrix = replace_zeros(matrix)
print_matrix(matrix)
print(count_ones(matrix))
print(commands)
