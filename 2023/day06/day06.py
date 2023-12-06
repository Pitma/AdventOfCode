# from collections import *
# from itertools import *
# from math import *
#from submit_answer import submit_answer
import re
import numpy as np


#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [288, 71503]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    #A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    A = input_string
    N = len(A)
    print("N =", N)
    time_distance_map={}
    lines = input_string.splitlines()

    for time, distance in zip(lines[0].split()[1:], lines[1].split()[1:]):
        
        time_distance_map[int(time)] = int(distance)

    result=[]
    for time, distances in time_distance_map.items():
        print(f"Time: {time}, Distances: {distances}")
        counter=0
        for i in range(time+1):
            speed = i
            remain = time - i
            record = speed*remain

            if record > int(distances):
                counter += 1
        result.append(counter)

    if LEVEL == 1:
        return np.prod(result)
    else:
        return np.prod(result)


def main():
    with open("sample.txt") as sample_file:
        sample_input = sample_file.read().strip('\n')
    sample_answer = solve(sample_input)
    print("Answer for sample:", sample_answer)
    assert sample_answer == SAMPLE_ANSWER and sample_answer is not None, f"Got {sample_answer} instead of {SAMPLE_ANSWER}"
    #return
    with open("input.txt") as input_file:
        inp = input_file.read().strip('\n')
    answer = solve(inp)
    print("Answer:", answer)
    #assert submit_answer(2023, 06, LEVEL, answer) is True


if __name__ == '__main__':
    main()