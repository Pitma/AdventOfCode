from collections import defaultdict, Counter

file = "inputTest.txt"

start = "NNCB"
# start = "KKOSPHCNOCHHHSPOBKVF"

steps = 10

poly = defaultdict(list)

# load file and create dictionary
def load_file(file):
    with open(file) as f:
        for line in f:
            line = line.split("->")
            poly[line[0].strip()] = line[1].strip()


# create list with each two characters in start
def create_list(start):
    list = []
    for i in range(len(start) - 1):
        list.append(start[i : i + 2])
    return list


load_file(file)


def process(start):
    list = create_list(start)
    newStart = ""
    for j in list:
        if j in poly:
            newStart += "".join(j[0])
            newStart += poly[j]
            last = "".join(j[1])
            poly[j] = newStart
    newStart += last
    start = newStart
    return start


for i in range(steps):
    print("Step:", i)
    start = process(start)

# count occurences of each letter in start
count = Counter(start)
# get max value from count
max = count.most_common(1)[0][1]
# get min value from count
min = count.most_common()[-1][1]
print(max - min)
print(len(start))
# print(count)
# print(create_list(start))
# print(poly)
