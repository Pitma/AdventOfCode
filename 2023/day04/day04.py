# from collections import *
# from itertools import *
# from math import *
#from submit_answer import submit_answer
import numpy as np
import re


#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 1
SAMPLE_ANSWERS = [13, 30]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    #A = input_string

    N = len(A)
    print("N =", N)
    print(A[:10])
    # M = len(A[0])
    summe=0
    # for i in range(N):
    for line in A:
        hits=-1
        winnerList = np.char.split(re.findall(r':\s*([\d\s]+)\s*\|',line))[0]
        myList = np.char.split(re.findall(r'\|\s*([\d\s]+)\s*',line))[0]
        for i in range(len(myList)):
                if myList[i] in winnerList:
                    hits +=1
        if hits>=0:
            summe += 2**hits
    
    #Part II
    result_dict = {index: 1 for index in range(len(A))}
    print("dict: ",result_dict)
    for index,line in enumerate(A):
        hits=0
        print("index",index)
        winnerList = np.char.split(re.findall(r':\s*([\d\s]+)\s*\|',line))[0]
        myList = np.char.split(re.findall(r'\|\s*([\d\s]+)\s*',line))[0]

        for i in range(len(myList)):
            if myList[i] in winnerList:
                hits +=1
        for hit in range(1,hits+1):
            result_dict.update({index+hit:result_dict.get(index+hit)+(result_dict.get(index))})
        
        sum_of_values = sum(result_dict.values())

    for key, value in result_dict.items():
        if value == 0:
            result_dict[key] = 1

    if LEVEL == 1:
        return summe
    else:
        return sum_of_values


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
    #assert submit_answer(2023, 4, LEVEL, answer) is True


if __name__ == '__main__':
    main()