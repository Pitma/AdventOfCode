from collections import ChainMap
file = open("input.txt","r")
file_data = file.read()
lettersLow ={chr(i+96):i for i in range(1,27)}
lettersHigh = {chr(i+38):i for i in range(27,53)}
letters = ChainMap(lettersLow,lettersHigh)
input = file_data.split("\n")
priority = 0

print("Länge: ", len(input))
amount = len(input)
for i in range(0,amount-2,3):
    for char in input[i]:
        if  input[i].count(char)>0 and input[i+1].count(char)>0 and input[i+2].count(char)>0:
            priority += letters.get(char)
            break  

print("Final :",priority)




