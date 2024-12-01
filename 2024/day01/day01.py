# from collections import *
# from itertools import *
# from math import *
#from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [11, 31]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    #A = [line for line in input_string.split('\n')]
    A = input_string.split('\n')
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    #A = input_string
    N = len(A)
    print("N =", N)
    print(A[:10])
    # M = len(A[0])
    first_numbers = []
    second_numbers = []
    for line in A:
        num1, num2 = map(int, line.split())
        first_numbers.append(num1)
        second_numbers.append(num2)
    
    first_numbers.sort()
    second_numbers.sort()

    differences = []
    for i in range(len(first_numbers)):
        diff = abs(first_numbers[i] - second_numbers[i])
        differences.append(diff)
    
    
    #Part 2
    occurrences = []
    for num in first_numbers:  # Verwende set() um jede Zahl nur einmal zu prüfen
        count = second_numbers.count(num)
        occurrences.append(count * num)

    if LEVEL == 1:
        return sum(differences)
    else:
        return sum(occurrences)


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
    #assert submit_answer(2024, 01, LEVEL, answer) is True


if __name__ == '__main__':
    main()