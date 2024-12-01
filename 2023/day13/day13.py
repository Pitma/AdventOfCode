# from collections import *
# from itertools import *
# from math import *
#from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [405, 400]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]

def compare(row1, row2):
    differences = 0

    for char1, char2 in zip(row1, row2):
        if char1 != char2:
            differences += 1
            if differences > 1:
                break
        else:
            continue
    
    if differences == 1:
        return True
    else:
        return False 
    
def check_rows(grid,one,two):
    #print("one",one,"two",two)
    if grid[one] == grid[two]:
        return True
    else:
        if LEVEL ==2:
            if compare(grid[one],grid[two]):
                print("Smudge gefunden")
                return True
        return False
    
def find_symmetry(grid,multiplier):
    rows = len(grid)
    #print("Grid",grid)
    #print("lenRoww",rows)
    found= False
    check = 0
    for i in range(rows - 1):
        #print("testing",i)
        current_row = grid[i]
        next_row = grid[i + 1]
        if current_row == next_row:
            check = i+1
            found = True
            start_row = i
            end_row = i+1
            while (start_row >= 0 and end_row <= len(grid)-1) :
                print(start_row,end_row)
                found = check_rows(grid,start_row,end_row)
                print(found)
                start_row -= 1
                end_row += 1
                if found:
                    continue
                else:
                    break
                    #check = 0

            if (start_row<0 or end_row > len(grid)) and found:
                print("end reached")
                break
    if found:
        value = (check)*multiplier
        return value
    else: 
        return 0
    
    
def vertical_to_horizontal(grid):
    #transposed_grid = [row[::-1] for row in grid]
    transposed_grid = ["".join(row) for row in zip(*grid)]
    #print(transposed_grid)
    return transposed_grid

def solve(input_string: str) -> int or str:

    A = [line.split('\n')  for line in input_string]
    N = len(A)
    print("N =", N)

    sum = 0

    for grids in A:
        sum += find_symmetry(grids,100)
        #print("sum1 vertical",sum)
        transposed_grid = vertical_to_horizontal(grids)
        sum += find_symmetry(transposed_grid,1)
        #print("sum2 horizontal",sum,1)
        print("-----------")

    if LEVEL == 1:
        return sum
    else:
        return sum


def main():
    with open("sample.txt") as sample_file:
        sample_input = sample_file.read().split('\n\n')
    sample_answer = solve(sample_input)
    print("Answer for sample:", sample_answer)
    assert sample_answer == SAMPLE_ANSWER and sample_answer is not None, f"Got {sample_answer} instead of {SAMPLE_ANSWER}"
    #return
    with open("input.txt") as input_file:
        inp = input_file.read().split('\n\n')
    answer = solve(inp)
    print("Answer:", answer)


if __name__ == '__main__':
    main()