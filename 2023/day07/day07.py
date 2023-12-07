# from collections import *
# from itertools import *
# from math import *
#from submit_answer import submit_answer
from collections import Counter


#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [6440, 5905]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]

def rank(hand, part_2=False):
    # Special-case JJJJJ; other hands Js just become the most common card.
    if part_2 and hand != 'JJJJJ':
        no_jokers = Counter(c for c in hand if c != 'J').most_common()
        hand = hand.replace('J', no_jokers[0][0])

    cmn = Counter(hand).most_common()

    # Five of a Kind
    if cmn[0][1] == 5:
        return 6

    # Four of a Kind
    elif cmn[0][1] == 4:
        return 5

    # Full House / Three of a Kind (based on second-most common card)
    elif cmn[0][1] == 3:
        return 2 + cmn[1][1]

    # Two Pair / One Pair (based on second-most common card)
    elif cmn[0][1] == 2:
        return cmn[1][1]

    return 0


def tiebreak(hand, part_2=False):
    return tuple(card_score(c, part_2) for c in hand)


def card_score(card, part_2=False):
    if part_2:
        return 'J23456789TQKA'.index(card)
    else:
        return '23456789TJQKA'.index(card)

def solve(input_string: str) -> int or str:
    hands =[]
    for line in input_string:
        hand, bid = line.split()
        hands.append((hand, int(bid)))
    #A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    #A = [line for line in input_string.split(' ')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    A = input_string
    N = len(A)
    print("N =", N)
    #print(A)
    # Solve part 1.
    part_1 = 0
    for i, (hand, bid) in enumerate(sorted(hands, key=lambda h: (rank(h[0]), tiebreak(h[0]))), start=1):
        part_1 += i * bid

    print("Part 1:", part_1)


    # Solve part 2.
    part_2 = 0
    for i, (hand, bid) in enumerate(sorted(hands, key=lambda h: (rank(h[0], part_2=True), tiebreak(h[0], part_2=True))), start=1):
        part_2 += i * bid
        

    if LEVEL == 1:
        return part_1
    else:
        return part_2


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
    #assert submit_answer(2023, 07, LEVEL, answer) is True


if __name__ == '__main__':
    main()