import re
file = open("input.txt","r")
file_data = file.read()
sum = 0

input = file_data.split("\n")

print(input)
for line in input: 
    print('Line',line)
    #cheese it
    newLine = re.sub('one','1',line)
    newLine = re.sub('tw','2',newLine)
    newLine = re.sub('three','3',newLine)
    newLine = re.sub('four','4',newLine)
    newLine = re.sub('five','5',newLine)
    newLine = re.sub('six','6',newLine)
    newLine = re.sub('seven','7',newLine)
    newLine = re.sub('igh','8',newLine)
    newLine = re.sub('nine','9',newLine)
    print('NewLine',newLine)
    matches = re.findall(r'\d',newLine)
    calc = matches[0]+matches[len(matches)-1]
    print('Calc',calc) 

    sum = sum + int(calc)

print('Result:', sum)


