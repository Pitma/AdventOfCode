def p1(f):
    ans = 0

    def find(lines):
        for i in range(1, len(lines)):
            if all(a == b for a, b in zip(lines[:i][::-1], lines[i:])):
                return i

    for index,thing in enumerate(f.read().split("\n\n")):
        thing = thing.splitlines()
        if v := find([*zip(*thing)]):
            #print([*zip(*thing)])
            ans += v
        if h := find(thing):
            ans += h * 100
        print(index,ans)
    return ans


def p2(f):
    ans = 0

    def find(lines):
        for i in range(1, len(lines)):
            differs = sum(
                ax != bx
                for a, b in zip(lines[:i][::-1], lines[i:])
                for ax, bx in zip(a, b)
            )
            if differs == 1:
                return i

    for thing in f.read().split("\n\n"):
        thing = thing.splitlines()
        if v := find([*zip(*thing)]):
            ans += v
        if h := find(thing):
            ans += h * 100

    return ans

with open("sample.txt") as sample_file:
    p1(sample_file)