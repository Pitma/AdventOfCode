from collections import *
# from itertools import *
from math import gcd

#from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [6, 6]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]

def direction(dir):
    if dir == 'L':
        return 0
    return 1
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def calculate_lcm(numbers):
    lcm_factors = Counter()
    
    for num in numbers:
        factors_count = Counter(prime_factors(num))
        lcm_factors = lcm_factors | factors_count

    lcm = 1
    for factor, count in lcm_factors.items():
        lcm *= factor ** count

    return lcm

def solve(input_string: str) -> int or str:
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    #A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    A = input_string
    N = len(A)
    print("N =", N)
    print(A[:10])
    # M = len(A[0])
    my_map = {}
    ghostList = []
    commands = None
    # for i in range(N):

    for line in input_string:
        parts = line.split('=')
        key = parts[0].strip()
        
        if commands is None:
            commands = key
        
        try:
            
            value = parts[1].strip(' \n()')
            my_map[key] = list(map(str.strip, value.split(',')))
            if key[-1] == 'A':
                ghostList.append(key)
        except:
            continue

        my_map[key] = list(map(str.strip, value.split(',')))
            
                    
    start = '11A'
    end = '11Z'
    count = 0
    breaker = True    
    print(my_map)
    print(ghostList)
    print(commands)
    print(start)

    while breaker and LEVEL == 1:
        
        for command in commands:
            #print(direction(command))
            #print("MAP:",my_map.get(start))
            start = my_map.get(start)[direction(command)]
            print(start)
            count+=1
            if start == end:
                breaker = False
    if LEVEL == 2:
        z = []
        for index,start in enumerate(ghostList):
            count=0
            breaker = True
            while breaker:
                
                for command in commands:
                    count+=1
                    start = my_map.get(start)[direction(command)]
                    ghostList[index] = start
                    if start.endswith('Z'):
                        z.append(count)
                        breaker = False
        print(z)
    if LEVEL == 1:
        return count
    else:
        return calculate_lcm(z)


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
    #assert submit_answer(2023, 08, LEVEL, answer) is True


if __name__ == '__main__':
    main()