import re
file = open("input.txt","r")
file_data = file.read()
loops = 14
input =  [*file_data]
check = []

#print(input)
for pos in range(0,len(input)):

        fail = 0
        for c in range(loops):
            check.extend(input[pos+c])
        print("POS:",pos,"CHECK",check)
        if len(list(set(check))) == loops:
            print("Ergebnis: ",pos+loops)
            break
        check.clear()











