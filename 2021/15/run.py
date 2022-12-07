import heapq
file = "input.txt"


with open(file) as f:
    input = [list(map(int, line.replace(" ", "").replace("\n", "")))
             for line in f]

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
print(vis)
