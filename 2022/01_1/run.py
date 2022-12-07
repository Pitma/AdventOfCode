import numpy as np
file = open("input.txt","r")
file_data = file.read()
max_load = 0

input = file_data.split("\n\n")

for line in input:
    linearray =  list(map(int,line.split()))
    
    if sum(linearray)>max_load:
        max_load = sum(linearray)

print(max_load)
