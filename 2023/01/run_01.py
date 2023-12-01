import re
file = open("input.txt","r")
file_data = file.read()
sum = 0

input = file_data.split("\n")

print(input)
for line in input: 
    matches = re.findall(r'\d',line)
    calc = matches[0]+matches[len(matches)-1]
    print(calc) 

    sum = sum + int(calc)

print('Result:', sum)


