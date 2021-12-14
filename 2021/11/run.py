import sys
from typing import Counter

sys.setrecursionlimit(10 ** 6)

grid_width = 10
grid_height = 10
file = "input.txt"
cycles = 100
flashCount = 0


def read_file(file):
    with open(file, "r") as f:
        grid = [[0 for x in range(grid_width)] for y in range(grid_height)]
        for i in range(grid_height):
            for j in range(grid_width):
                grid[j][i] = int(f.read(1).rstrip().replace("\n", ""))
    return grid


visited = []


def flash(grid):
    isFlash = False
    for i in range(grid_height):
        for j in range(grid_width):
            if grid[j][i] > 9 and [j, i] not in visited:
                isFlash = True
                visited.append([j, i])
                # increase surrounding cells by 1
                if i > 0:
                    grid[j][i - 1] = grid[j][i - 1] + 1  # top
                if i < grid_height - 1:
                    grid[j][i + 1] = grid[j][i + 1] + 1  # bottom
                if j > 0:
                    grid[j - 1][i] = grid[j - 1][i] + 1  # left
                if j < grid_width - 1:
                    grid[j + 1][i] = grid[j + 1][i] + 1  # right
                if i > 0 and j > 0:
                    grid[j - 1][i - 1] = grid[j - 1][i - 1] + 1  # top left
                if i > 0 and j < grid_width - 1:
                    grid[j + 1][i - 1] = grid[j + 1][i - 1] + 1  # top right
                if i < grid_height - 1 and j > 0:
                    grid[j - 1][i + 1] = grid[j - 1][i + 1] + 1  # bottom left
                if i < grid_height - 1 and j < grid_width - 1:
                    grid[j + 1][i + 1] = grid[j + 1][i + 1] + 1  # bottom right

    if isFlash:
        grid = flash(grid)
    return grid


def afterFlash(grid):
    counter = 0
    for i in range(grid_height):
        for j in range(grid_width):
            if grid[j][i] > 9:
                grid[j][i] = 0
                counter += 1
    return grid, counter


def increase_energy(grid):
    for i in range(grid_height):
        for j in range(grid_width):
            grid[j][i] = grid[j][i] + 1
    grid = flash(grid)
    return grid


grid = read_file(file)

score = 0
for i in range(cycles):
    print("Cycle: " + str(i))

    newGrid = increase_energy(grid)

    grid, counter = afterFlash(newGrid)
    score += counter
    for col in range(grid_width):
        board_grid = ""
        for row in range(grid_height):
            board_grid += str(grid[row][col])
        print(board_grid)
    visited = []
    print("Score: " + str(score))
