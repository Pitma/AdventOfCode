# from collections import *
from itertools import *
# from math import *
#from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [374, 8410]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]

def print_map(map_list):
    for row in map_list:
        print("".join(row))

def process_map(map_list):
    # Initialize lists to store indices of rows and columns to duplicate
    rows_to_duplicate = []
    cols_to_duplicate = []

    # Check rows for '#'
    for i, row in enumerate(map_list):
        if '#' not in row:
            rows_to_duplicate.append(i)

    # Check columns for '#'
    for j in range(len(map_list[0])): # assuming all rows have the same length
        col = [row[j] for row in map_list]
        if '#' not in col:
            cols_to_duplicate.append(j)

    # Duplicate rows with '.'
    for i in rows_to_duplicate:
        map_list.insert(i+1, ['.' for _ in map_list[0]])

    # Duplicate columns with '.'
    for j in cols_to_duplicate:
        for row in map_list:
            row.insert(j+1, '.')

    return map_list

def calculate_distances(array):

    grid = [line for line in array]
    double_y = {i for i, line in enumerate(grid) if "#" not in line}
    double_x = {j for j in range(len(grid[0])) if "#" not in [line[j] for line in grid]}
    print_map(grid)
    galaxies = {(i, j) for i, l in enumerate(grid) for j, c in enumerate(l) if c == "#"}
    print("pts",galaxies)
    
    if LEVEL==1:
        return sum(
            abs(p[0] - q[0])
            + abs(p[1] - q[1])
            + len(double_y & set(range(min(p[0], q[0]), max(p[0], q[0]) + 1)))
            + len(double_x & set(range(min(p[1], q[1]), max(p[1], q[1]) + 1)))
            for p, q in combinations(galaxies, 2)
        )
    if LEVEL ==2:
        return sum(
            abs(p[0] - q[0])
            + abs(p[1] - q[1])
            + 999999 * len(double_y & set(range(min(p[0], q[0]), max(p[0], q[0]) + 1)))
            + 999999 * len(double_x & set(range(min(p[1], q[1]), max(p[1], q[1]) + 1)))
            for p, q in combinations(galaxies, 2)
    )


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    #A = [line for line in input_string.split('\n')]
    A = [list(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    #A = input_string
    N = len(A)
    print("N =", N)
    #print(A)
    #print_map(A)
    #modified_map = process_map(A)
  
    #print_map(modified_map)
    distance = calculate_distances(A)

    # M = len(A[0])

    # for i in range(N):


    # for i in range(N):

    if LEVEL == 1:
        return distance
    else:
        return distance


def main():
    with open("sample.txt") as sample_file:
        sample_input = sample_file.read()
    sample_answer = solve(sample_input)
    print("Answer for sample:", sample_answer)
    #assert sample_answer == SAMPLE_ANSWER and sample_answer is not None, f"Got {sample_answer} instead of {SAMPLE_ANSWER}"
    #return
    with open("input.txt") as input_file:
        inp = input_file.read()
    answer = solve(inp)
    print("Answer:", answer)
    #assert submit_answer(2023, 11, LEVEL, answer) is True


if __name__ == '__main__':
    main()