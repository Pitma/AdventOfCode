# from collections import *
# from itertools import *
# from math import *
#from submit_answer import submit_answer
from collections import defaultdict
import numpy as np
import re



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [4361,467835]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]

hitList = []

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    # A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    #A = [list(map(str, line)) for line in input_string.split('\n')]
    A = input_string
    N = len(A)
    print("N =", N)
    #print(A[:10])
    total_sum = 0
    adjacent_numbers = defaultdict(list)
    if LEVEL == 1:

        for row_index, line in enumerate(A):
            for match in re.finditer(r"\d+", line):
                start, end = match.start() - 1, match.end()
                nearby_indices = [
                    (row_index, start),
                    (row_index, end),
                    *[(row_index - 1, col) for col in range(start, end + 1)],
                    *[(row_index + 1, col) for col in range(start, end + 1)]
                ]

                valid_indices = filter(lambda idx: 0 <= idx[0] < len(A) and 0 <= idx[1] < len(A[idx[0]]) and A[idx[0]][idx[1]] != ".", nearby_indices)
            
                count = sum(1 for _ in valid_indices)

                if count > 0:
                    total_sum += int(match.group())
        
        return total_sum
    else:
        
        # Durchlaufe jede Zeile in den Zeilen
        for row_index, line in enumerate(A):
            # Suche nach aufeinanderfolgenden Zahlen in der Zeile
            for match in re.finditer(r"\d+", line):
                # Berechne Indizes rund um die gefundene Zahl
                start, end = match.start() - 1, match.end()
                nearby_indices = [
                    (row_index, start),
                    (row_index, end),
                    *[(row_index - 1, col) for col in range(start, end + 1)],
                    *[(row_index + 1, col) for col in range(start, end + 1)]
                ]

                # Überprüfe die Gültigkeit der Indizes und füge die Zahl der Liste hinzu
                for a, b in nearby_indices:
                    if 0 <= a < len(A) and 0 <= b < len(A[a]) and A[a][b] != ".":
                        adjacent_numbers[a, b].append(match.group())

        # Berechne die Summe der Produkte der benachbarten Zahlen
        total_sum = sum(int(x[0]) * int(x[1]) for x in adjacent_numbers.values() if len(x) == 2)

        return total_sum



def main():
    with open("sample.txt") as sample_file:
        sample_input = sample_file.read().splitlines()
    sample_answer = solve(sample_input)
    print("Answer for sample:", sample_answer)
    assert sample_answer == SAMPLE_ANSWER and sample_answer is not None, f"Got {sample_answer} instead of {SAMPLE_ANSWER}"
    with open("input.txt") as input_file:
        inp = input_file.read().splitlines()
    answer = solve(inp)
    print("Answer:", answer)
    #assert submit_answer(2023, 03, LEVEL, answer) is True


if __name__ == '__main__':
    main()