import heapq
file = "inputTest.txt"


with open(file) as f:
    input = [list(map(int, line.replace(" ", "").replace("\n", "")))
             for line in f]

r = len(input[0])
c = len(input)

for i in range(4):
    jump = i*r
    list = []
    for col in range(c):
        for row in range(r):
            if input[col][row+jump] + 1 == 10:
                input[row].append(1)
            else:
                input[row].append(input[col][row+jump]+1)


r = len(input[0])
c = len(input)-1

for i in range(4):
    jump = i*c
    for col in range(c):
        list = []
        for row in range(r):
            #
            if input[col][row] + 1 == 10:
                # input[row].append(1)
                list.append(1)
            else:
                # input[row].append(input[col][row+jump]+1)
                list.append(input[col][row]+1)
        input.append(list)


print(input)
exit(0)
paths = [(0, 0, 0)]

vis = [[0] * len(row) for row in input]

while True:
    rf, x, y = heapq.heappop(paths)
    if vis[x][y]:
        continue
    if (x, y) == (len(input) - 1, len(input[x]) - 1):
        print(rf)
        break
    vis[x][y] = 1
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if not len(input) > nx >= 0 <= ny < len(input[0]):
            continue
        if vis[nx][ny]:
            continue
        heapq.heappush(paths, (rf + input[nx][ny], nx, ny))

print(input)
# print(vis)
