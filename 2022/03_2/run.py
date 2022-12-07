from collections import ChainMap
file = open("input.txt","r")
file_data = file.read()
lettersLow ={chr(i+96):i for i in range(1,27)}
lettersHigh = {chr(i+38):i for i in range(27,53)}
letters = ChainMap(lettersLow,lettersHigh)
input = file_data.split("\n")
priority = 0

for line in input:
    part1 = slice(0,len(line)//2)
    part2 = slice(len(line)//2,len(line))
    for char in line[part1]:
       count = line[part2].count(char)
       if count>0:
        priority += letters.get(char)
        print(priority)
        break

print(priority)




