# from collections import *
from itertools import *
from functools import cache
# from math import *
#from submit_answer import submit_answer
# 1566786613613 



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [21, 525152]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]

def find_combinations(input):
    cnt = 0

    for line in input:
        chars, numbers = line.split()
        numbers = [int(x) for x in numbers.split(",")]
        qmarks = [i for i, c in enumerate(chars) if c == "?"]
        #print(qmarks)
        for combination in combinations(qmarks, sum(numbers) - chars.count("#")):
            #print(combination)
            possible_chars = "".join("#" if i in combination else c for i, c in enumerate(chars))
            print(possible_chars)
            possible_nums = [len(t) for t in possible_chars.replace("?", ".").split(".") if t]
            print(possible_nums)
            if numbers == possible_nums:
                cnt += 1

    return cnt

def generate_combinations(iterable, r): 
    pool = tuple(iterable) 
    n = len(pool) 
    if r > n: 
        return 
    indices = list(range(r)) 
    yield tuple(pool[i] for i in indices) 
    while True:
        for i in reversed(range(r)): 
            if indices[i] != i + n - r: 
                break 
            else: 
                return 
        indices[i] += 1 
        for j in range(i+1, r): 
            indices[j] = indices[j-1] + 1 
        yield tuple(pool[i] for i in indices)

def find_combinations2(input_lines):
    cnt = 0
    for line in input:
        chars, numbers = line.split()
        chars = "".join(chars+"?")*5
        chars = chars[:-1]
        print(chars)
        numbers = [int(x) for x in numbers.split(",")]*5
        #print("numbers",numbers)
        qmarks = [i for i, c in enumerate(chars) if c == "?"]
        #print("?",qmarks)
        for combination in combinations(qmarks, sum(numbers) - chars.count("#")):
            #print(combination)
            possible_chars = "".join("#" if i in combination else c for i, c in enumerate(chars))
            #print(possible_chars)
            possible_nums = [len(t) for t in possible_chars.replace("?", ".").split(".") if t]
            #print(possible_nums)
            #print(numbers)
            if numbers == possible_nums:
                cnt += 1

    return cnt

def compute(input: str):
    res = 0
    for line in input:
        d, ns = line.split()
        ns = tuple(map(int, ns.split(',')))
        d = '?'.join([d]*5)
        ns = ns*5
        d += '.'
        cnt = count(d, ns)
        res += cnt
    return res

@cache
def count(d, ns):
    if ns == ():
        return 0 if '#' in d else 1
    dlen = len(d)
    nslen = len(ns)
    n = ns[0]
    res = 0
    for i in range(dlen-(nslen-1+sum(ns[1:]))-(n+1)+1):
        if d[i+n] == '#':
            continue
        if '#' in d[:i]:
            break
        if '.' not in d[i:i+n]:
            res += count(d[i+n+1:], ns[1:])
    return res

def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    #A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    A = input_string
    #N = len(A)
    #print("N =", N)
    #print(A[:10]) 
    # M = len(A[0])
    #print(p1(A))
    # for i in range(N):


    # for i in range(N):

    if LEVEL == 1:
        return find_combinations(A)
    else:
        return compute(A)


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
    #assert submit_answer(2023, 12, LEVEL, answer) is True


if __name__ == '__main__':
    main()