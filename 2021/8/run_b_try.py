from itertools import *


# read lines from file
def read_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


t = 0

lines = read_lines("inputTest.txt")

for k in lines:
    a, b = k.split(" | ")
    do = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]
    req = set(do)

    # print(req)
    for x in permutations("abcdefg"):
        m = {i: j for i, j in zip(x, "abcdefg")}
        print(m)
        r = {"".join(sorted(map(m.get, q))) for q in a.split()}
        print(r)
        if r == req:
            b = ["".join(sorted(map(m.get, q))) for q in b.split()]
            b = "".join(str(do.index(q)) for q in b)
            t += int(b)

print(t)
