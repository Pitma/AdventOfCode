from typing import MutableMapping


inputs = []
# read all values from inputTest.txt and split by ""
# an remove leading and trailing whitespace and
# an remove "\n" from each line
with open("input.txt", "r") as f:
    for line in f:
        inputs.append(line.split())

col = 100
row = len(inputs)

heights = ""
for value in inputs:
    for char in value:
        heights += char
heights = heights.replace("\n", "")

grid = list(heights)


def index(i, j):
    return j + i * col


def checkNeighbours(i, j, height):

    counter = 0
    if j - 1 < 0:
        counter += 1
    elif grid[index(i, j - 1)] > height:
        counter += 1
    if j + 1 >= col:
        counter += 1
    elif grid[index(i, j + 1)] > height:
        counter += 1
    if i - 1 < 0:
        counter += 1
    elif grid[index(i - 1, j)] > height:
        counter += 1
    if i + 1 >= row:
        counter += 1
    elif grid[index(i + 1, j)] > height:
        counter += 1
    if counter >= 4:
        return True

    return False


cell_counters = []


def countBasinCells(i, j, grid):

    counter = 0
    if int(grid[index(i, j)]) < 9:
        counter += count_basin_cells(i, j, grid)
    cell_counters.append(counter)
    return counter


r = []


def count_basin_cells(i, j, grid):
    if any([i < 0, j < 0, i >= row, j >= col]):
        return 0
    if grid[index(i, j)] == 9:
        return 0
    cell_count = 1
    grid[index(i, j)] = 9

    if j - 1 < 0:
        print("")
    elif int(grid[index(i, j - 1)]) < 9:
        cell_count += count_basin_cells(i, j - 1, grid)
    if j + 1 >= col:
        print("")
    elif int(grid[index(i, j + 1)]) < 9:
        cell_count += count_basin_cells(i, j + 1, grid)
    if i - 1 < 0:
        print("")
    elif int(grid[index(i - 1, j)]) < 9:
        cell_count += count_basin_cells(i - 1, j, grid)
    if i + 1 >= row:
        print("")
    elif int(grid[index(i + 1, j)]) < 9:
        cell_count += count_basin_cells(i + 1, j, grid)
    r.append(cell_count)
    return cell_count


class Cell:
    def __init__(self, i, j, height):
        self.i = i
        self.j = j
        self.height = height
        self.visited = False


class Basin:
    def __init__(self, i, cell):
        self.id = i
        self.cells = [cell]


c = 0
basins = []
for i in range(row):
    for j in range(col):
        if checkNeighbours(i, j, grid[index(i, j)]):
            c = c + int(grid[index(i, j)]) + 1
            basins.append(Basin(i, Cell(i, j, grid[index(i, j)])))


def multiplyList(myList):

    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# check all cells in basins and check theire neighbours if they are < 9

for basin in basins:
    for cell in basin.cells:
        if checkNeighbours(cell.i, cell.j, cell.height):
            c = c + int(cell.height) + 1

final = 1
print(c)
for basin in basins:
    for cell in basin.cells:
        c = countBasinCells(cell.i, cell.j, grid)
        final = final * c
# order cell_counters and multiply the 3 highest
cell_counters.sort()
print(multiplyList(cell_counters[-3:]))
