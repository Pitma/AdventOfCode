# from collections import *
# from itertools import *
# from math import *
#from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [6440, 5905]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]


def solve(input_string: str) -> int or str:
    #A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    #A = [line for line in input_string.split(' ')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    A = input_string
    N = len(A)
    print("N =", N)
    #print(A)
    # Werte aus der Datei extrahieren und verarbeiten
    data_map = {}
    #card_values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    if LEVEL ==1:
        card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    else:
        card_values = ['J','2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    
    for line in A:
        # Die Werte trennen und Leerzeichen entfernen
        values = line.strip().split()
        
        # Wenn es mindestens zwei Werte gibt
        if len(values) >= 2:
            cards = values[0]  # Der erste Wert wird als "cards" verwendet
            bid = ' '.join(values[1:])  # Der Rest wird als "bid" verwendet
            
           

            # Ein neues Dictionary für die Zeile erstellen und in die Map einfügen
            row_data = {'cards': cards, 'bid': bid}
            
            card_count = {}
            for card in cards:
                card_count[card] = card_count.get(card, 0) + 1
            row_data['card_count'] = card_count

        # Überprüfen, ob es ein Full House ist und Punkte vergeben
        points = 0
        #if 5 in card_count.values() :
            #points = 7 
        if 4 in card_count.values() :
            points = 6
        elif 3 in card_count.values() and 2 in card_count.values():
             points = 5  
             if int(card_count.get('J') or 0) > 0:
                points +=1
                #print("ja hat Joker",values)
            
        elif 3 in card_count.values() and 2 not in card_count.values():
            points = 4  
            if int(card_count.get('J') or 0) > 1:
                points +=2
            elif int(card_count.get('J') or 0) == 1:
                points +=1
                #print("ja hat Joker",values)
        elif list(card_count.values()).count(2) == 2:
            points = 3
            #print(card_count.get('J'))
            if int(card_count.get('J') or 0) > 1 :
                    points +=3
                    #print("ja hat Joker",values)

        elif list(card_count.values()).count(2) == 1:
            points = 2
            if int(card_count.get('J') or 0) == 1:
                points +=2
                #print("ja hat Joker",values)    
        else:
            points = 1
            if card_count.get('J') == 1:
                points +=1
                #print("ja hat Joker",values)    

        row_data['points'] = points
        data_map[values[0]] = row_data
    # Die Liste nach Punkten sortieren
    sorted_list = sorted(data_map.items(), key=lambda x: (x[1]['points'], [card_values.index(card) for card in x[1]['cards']]), reverse=True)

    #print(sorted_list)
    count=len(sorted_list)
    total=0
    for row_index,card in sorted_list:
        #print("index",row_index)
        total += count * int(card.get('bid'))
        count -= 1
        
    # M = len(A[0])
    # 248465995 too high
    # for i in range(N):


    # for i in range(N):

    if LEVEL == 1:
        return total
    else:
        return total


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