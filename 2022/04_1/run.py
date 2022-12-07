import re
file = open("input.txt","r")
file_data = file.read()
values = []
input = [r.split(',') for r in file_data.split('\n')] # file_data.split("\n")
count = 0

def checkRange(l1,h1,l2,h2):
    if l1 in range(l2,h2+1) and h1 in range(l2,h2+1):
        print("bäm in Range")
        return 1
    elif l2 in range(l1,h1+1) and h2 in range(l1,h1+1):
        print("bäm noch ein Range")
        return 1
    return 0

for v in input:
    values.append([v[0].split('-'),(v[1].split('-'))])

for k,p in values:
    count += checkRange(int(k[0]),int(k[1]),int(p[0]),int(p[1]))
    print("K: ",k,"P:",p)



print(count)




