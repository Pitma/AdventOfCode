import re
file = open("input.txt","r")
file_data = file.read()
#stacks = [["N","Z"],["D","C","M"],["P"]]
stacks = [
    ["P","V","Z","W","D","T"],
    ["D","J","F","V","W","S","L"],
    ["H","B","T","V","S","L","M","Z"],
    ["J","S","R"],
    ["W","L","M","F","G","B","Z","C"],
    ["B","G","R","Z","H","V","W","Q"],
    ["N","D","B","C","P","J","V"],
    ["Q","B","T","P"],
    ["C","R","Z","G","H"]
    ]
input =  file_data.split("\n")
count = 0
print("Start: ",stacks)
count=0
print(input)
for command in input:
    commands = []
    commands = re.findall(r'\d+',command)
    
    commands = list(map(int, commands))
    count += 1
    print(count)
    for i in range(commands[0]):
        value = stacks[commands[1]-1].pop(0)
        #print("Nach POP:",stacks)
        stacks[commands[2]-1].insert(0,value)
        #print("Nach Insert:",stacks)
        
print("Ergebnis:")
for result in stacks:
    print(result[0])







