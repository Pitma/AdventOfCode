def vertical_to_horizontal(grid):
    transposed_grid = [row[::-1] for row in grid]
    return transposed_grid

grid = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#."
]

transposed_grid = vertical_to_horizontal(grid)

for row in transposed_grid:
    print(row)