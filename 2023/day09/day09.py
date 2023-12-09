# from collections import *
from itertools import *
import math
#from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [114, 2]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]

def seq(ints):
    # Überprüfe, ob alle Elemente in der Liste ints gleich null sind
    if all(ints == 0 for ints in ints):
        return 0  # Wenn ja, gebe 0 zurück
    # Berechne die Paarweisen Differenzen der Elemente in ints
    diffs = [b - a for a, b in pairwise(ints)]
    
    # Füge das letzte Element von ints zur rekursiven Anwendung der seq-Funktion mit diffs hinzu
    return ints[-1] + seq(diffs)

def solve(input_string: str) -> int or str:
    #A = list(input_string)
    #A = list(map(int, input_string.split()))
    #A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    A = input_string
    N = len(A)
    print("N =", N)
    #print(A[:10])
    # M = len(A[0])
    sum=0
    for history in A:
        number = seq(list(map(int,history.split())))
        sum+=number
    
    sum2=0
    for history in A:
        number = seq(list(map(int,history.split()[::-1])))
        sum2+=number

    # for i in range(N):

    if LEVEL == 1:
        return sum
    else:
        return sum2


def main():
    with open("sample.txt") as sample_file:
        sample_input = sample_file.readlines()
    sample_answer = solve(sample_input)
    print("Answer for sample:", sample_answer)
    assert sample_answer == SAMPLE_ANSWER and sample_answer is not None, f"Got {sample_answer} instead of {SAMPLE_ANSWER}"
    #return
    with open("input.txt") as input_file:
        inp = input_file.readlines()
    answer = solve(inp)
    print("Answer:", answer)
    #assert submit_answer(2023, 09, LEVEL, answer) is True


if __name__ == '__main__':
    main()