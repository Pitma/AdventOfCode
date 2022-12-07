import numpy as np
file = open("input.txt","r")
file_data = file.read()

max_load = []

input = file_data.split("\n\n")

for line in input:
    linearray =  list(map(int,line.split()))
    max_load.append(sum(linearray))
    
max_load.sort(reverse=True)
print(max_load[0] +max_load[1] + max_load[2])

