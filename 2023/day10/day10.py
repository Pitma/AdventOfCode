# from collections import *
# from itertools import *
# from math import *
#from submit_answer import submit_answer



#      N   E   S   W
chr = [-1, 0,  1,  0, -1, -1,  1,  1]
chc = [0,  1,  0, -1, -1,  1, -1,  1]


LEVEL = 2
SAMPLE_ANSWERS = [8, 4]
SAMPLE_ANSWER = SAMPLE_ANSWERS[LEVEL - 1]
loop =[]
def find_starting_point(input):
    for index,line in enumerate(input):
        for i in range(len(line)):
            if line[i] == 'S':
                loop.append([index,i])
                return index,i
            
def mod_starting_point(input_text):
    for index, line in enumerate(input_text):
        input_text[index] = list(line)  

        for i in range(len(input_text[index])):
            if input_text[index][i] == 'S':
                input_text[index][i] = '|' # needs to be adjusted according your Input to match the loop flow

        input_text[index] = ''.join(input_text[index])  

    return input_text

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)
neighbours = {
	'|': (up, down),
	'-': (left, right),
	'L': (up, right),
	'J': (up, left),
	'7': (down, left),
	'F': (down, right),
	'.': (),
}
found =False
def find_loop(input,start,direction=0,isStart = False):
    if isStart:
        for dir in range(4):
            try:
                row = start[0]+chr[dir]
                col = start[1]+chc[dir]
                hit = input[row][col]
            except:
                continue
            if row >=0 and col >= 0:
                if dir ==2 and hit in ("|","J","L"):
                    print("yo Süden geht")
                    rowCol,newDir =[row,col],"n"
                    break
                elif dir ==0 and hit in ("|","7","F"):
                    print("yo Norden geht")
                    rowCol,newDir =[row,col],"s"
                    break
                elif dir ==1 and hit in ("-","J","7"):
                    print("yo Osten geht")
                    rowCol,newDir = [row,col],"w"
                    break
                elif dir ==2 and hit in ("|","J","L"):
                    print("yo Süden geht")
                    rowCol,newDir =[row,col],"n"
                    break
                elif dir ==3 and hit in ("-","J","7"):
                    print("yo Westen geht",hit)
                    rowCol,newDir =[row,col],"o"
                    break
        return [rowCol,newDir]
    
    
    loop.append(start)
    #print("Start",start)
    row = start[0]
    col = start[1]
    rowCol = 0
    newDir = None
    value = input[row][col]
    #print(value)
    #print("direcction", direction,"value", value,"loop",loop)
    if value == "S":
        found = True
        print("Loop geschlossen")
        return None
    elif direction == "s":
        if value == "|":
            rowCol,newDir = [row-1,col],"s"
        if value == "7":
            rowCol,newDir = [row,col-1],"o"
        if value == "F":
            rowCol,newDir = [row,col+1],"w"
    elif direction == "w":
        if value == "-":
            rowCol,newDir = [row,col+1],"w"
        if value == "J":
            rowCol,newDir = [row-1,col],"s"
        if value == "7":
            rowCol,newDir = [row+1,col],"n"
    elif direction == "n":
        if value == "|":
            rowCol,newDir = [row+1,col],"n"
        if value == "J":
            rowCol,newDir = [row,col-1],"o"
        if value == "L":
            rowCol,newDir = [row,col+1],"w"
    elif direction == "o":
        if value == "-":
            rowCol,newDir = [row,col-1],"o"
        if value == "F":
            rowCol,newDir = [row+1,col],"n"
        if value == "L":
            rowCol,newDir = [row-1, col], "s"
    else: print("Shit ich bin lost")
    
    return [rowCol,newDir]

def solve(input_string: str) -> int or str:
    loop.clear()
    # A = list(input_string)
    # A = list(map(int, input_string.split(',')))
    A = [line for line in input_string.split('\n')]
    # A = [int(line) for line in input_string.split('\n')]
    # A = [list(map(int, line)) for line in input_string.split('\n')]
    #A = input_string
    N = len(A)
    print("N =", N)
    print(A[:10])
    #print(A)
    # M = len(A[0])
    row,column = find_starting_point(A)
    start = [row,column]
    res = find_loop(A,start,0,True)
    start = res[0]
    direction = res[1]
    #print("Result", res)

    while not found:
       try:
        start,direction = find_loop(A,start,direction)
       except:
           break
       
    #print(loop)
    result = (len(loop))//2

    A = mod_starting_point(A)
    cnt = 0
    for index,line in enumerate(A):
        print(index,line)
        for i in range(len(line)):
            if [index, i] in loop:
                #print('@', end='')
                continue
            inside = False
            for x2 in range(index, len(line)):
                if [x2, i] in loop and right in neighbours[A[x2][i]]:
                    inside = not inside
            if inside:
                cnt += 1
 

    if LEVEL == 1:
        return result
    else:
        return cnt


def main():
    with open("sample.txt") as sample_file:
        sample_input = sample_file.read().strip('\n')
    sample_answer = solve(sample_input)
    print("Answer for sample:", sample_answer)
    #assert sample_answer == SAMPLE_ANSWER and sample_answer is not None, f"Got {sample_answer} instead of {SAMPLE_ANSWER}"
    #return
    with open("input.txt") as input_file:
        inp = input_file.read().strip('\n')
    answer = solve(inp)
    print("Answer:", answer)
    #assert submit_answer(2023, 10, LEVEL, answer) is True


if __name__ == '__main__':
    main()