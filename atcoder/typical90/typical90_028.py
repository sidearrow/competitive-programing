split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
COORD_MAX = 1001
coord = [[0] * COORD_MAX for _ in range(COORD_MAX)]
for _ in range(N):
    lx, ly, rx, ry = split_int_input()
    coord[ly][lx] += 1
    coord[ly][rx] -= 1
    coord[ry][lx] -= 1
    coord[ry][rx] += 1

for y in range(COORD_MAX):
    for x in range(1, COORD_MAX):
        coord[y][x] += coord[y][x - 1]
for x in range(COORD_MAX):
    for y in range(1, COORD_MAX):
        coord[y][x] += coord[y - 1][x]

ans = [0] * N
for row in coord:
    for col in row:
        if col > 0:
            ans[col - 1] += 1

print(*ans, sep="\n")
