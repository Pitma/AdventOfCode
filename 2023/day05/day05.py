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
SAMPLE_ANSWERS = [35, 46]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]

def interpolate_map(map_data,seed):
        #print("aktueller Seed",seed)
        for i in range(len(map_data['src'])):
            src_start = map_data['src'][i]
            dest_start = map_data['dest'][i]
            length = map_data['length'][i]

            if seed >= src_start and seed < src_start + length:

                interpolated = (seed - src_start) + dest_start

                return interpolated
        return seed

def interpolate_reverse(map_data,seed):
    #print("aktueller Seed",seed)
    len(map_data['src'])
    for i in range(len(map_data['src'])):
        src_start = map_data['src'][i]
        dest_start = map_data['dest'][i]
        length = map_data['length'][i]

        if seed >= dest_start and seed < dest_start + length:

            interpolated = (seed - dest_start) + src_start

            return interpolated
    return seed

def is_in_ranges(number, seeds):
    for start, length in zip(seeds[0::2], seeds[1::2]):
        if number >= start and number < start + length:
            return True
    return False

def solve(input_string: str) -> dict:
    #A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    #A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    #A = [list(map(str, line)) for line in input_string.split('\n')]
    A = input_string.split("\n")
    N = len(A)
 
    print("N =", N)

    all_maps = {}
    current_title = None
    current_map = {"dest": [], "src": [], "length": []}
    seeds = []
    #setup
    for line in A:
        if line.startswith("seeds:"):
            # Ignoriere Zeilen mit "seeds:"
            seeds = list(map(int, line.split(":")[1].split()))
            #print("seeds:",seeds)
            continue
        if line.strip().endswith("map:"):
            #print("line",line)
            # Neuen Titeltext gefunden, aktuellen speichern und neuen initialisieren
            if current_title:
                all_maps[current_title] = current_map
            current_title = line.strip()
            current_map = {"dest": [], "src": [], "length": []}
        else:
        # Versuchen, Daten einzulesen und in die aktuelle Map schreiben
            try:
                data = list(map(int, line.split()))
                if len(data) == 3:
                    current_map["dest"].append(data[0])
                    current_map["src"].append(data[1])
                    current_map["length"].append(data[2])
                else:
                    continue
            except ValueError:
                continue

    # Die letzte Map speichern
    if current_title:
        all_maps[current_title] = current_map
    
    
    # Ergebnisse anzeigen
    low=None
    if LEVEL ==1:
        #PartI
        for seed in seeds:
            newSeed = seed
            for title, data in all_maps.items():
                newSeed = interpolate_map(data,newSeed)

            if low is None or newSeed < low:
                low = newSeed
    else:
        #PartII
        startSeed = 0
        found = False
        while not found:
            newSeed = startSeed
            for title, data in reversed(all_maps.items()):
                newSeed = interpolate_reverse(data,newSeed)
            if(is_in_ranges(newSeed,seeds)):
                print(f"{newSeed} in ranges: {is_in_ranges(newSeed, seeds)}")
                print("PartII Test:",newSeed)
                low = startSeed
                break
            else:
                startSeed+=1
                continue
            
        if low is None or newSeed < low:
            low = newSeed    

    # for i in range(N):

    if LEVEL == 1:
        return low
    else:
        return low


def main():
    with open("sample.txt") as sample_file:
        sample_input = sample_file.read()
    sample_answer = solve(sample_input)
    print("Answer for sample:", sample_answer)
    assert sample_answer == SAMPLE_ANSWER and sample_answer is not None, f"Got {sample_answer} instead of {SAMPLE_ANSWER}"
    #return
    with open("input.txt") as input_file:
        inp = input_file.read()
    answer = solve(inp)
    print("Answer:", answer)
    #assert submit_answer(2023, 05, LEVEL, answer) is True


if __name__ == '__main__':
    main()