from collections import defaultdict, Counter

file = "input.txt"

# start = "NNCB"
start = "KKOSPHCNOCHHHSPOBKVF"

steps = 40

dict = {}
counter = defaultdict(Counter)


def load_file(file):

    with open(file) as f:
        for line in f:
            line = line.strip()
            line = line.replace(" ", "")
            line1, line2 = line.split("->")
            dict[line1] = line2


load_file(file)

# create first counterinput
for i1, i2 in zip(start, start[1:]):
    counter[i1][i2] += 1
    print(counter)

# go through counter and and add 1 to each allocated value of polydict
# do this for as long as steps
for _ in range(steps):
    newCounter = defaultdict(Counter)
    for i1, value in counter.items():
        for i2, count in value.items():
            newCounter[i1][dict[i1 + i2]] += count
            newCounter[dict[i1 + i2]][i2] += count
    counter = newCounter
    print("Step:", _)


# max = count.most_common(1)[0][1]
print(dict)
print(counter)

sum = sum(counter.values(), Counter())
print(sum.most_common(1)[0][1] - sum.most_common()[-1][1])
