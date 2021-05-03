split_int_input = lambda: [int(v) for v in input().split()]

H, W, N, M = split_int_input()
denkyus = [split_int_input() for _ in range(N)]

field = [[0] * (W + 2) for _ in range(H + 2)]
for _ in range(M):
    r, c = split_int_input()
    field[r][c] = 1
for c in range(W + 2):
    field[0][c] = 1
    field[-1][c] = 1
for r in range(H + 2):
    field[r][0] = 1
    field[r][-1] = 1

for r, c in denkyus:
    if field[r][c] == 2:
        continue
    for i in range(r, H + 2):
        if field[i][c] == 1:
            break
        field[i][c] = 2
    for i in range(r, -1, -1):
        if field[i][c] == 1:
            break
        field[i][c] = 2

for r, c in denkyus:
    if field[r][c] == 3:
        continue
    for i in range(c, W + 2):
        if field[r][i] == 1:
            break
        field[r][i] = 3
    for i in range(c, -1, -1):
        if field[r][i] == 1:
            break
        field[r][i] = 3

ans = 0
for r in field:
    for v in r:
        if v >= 2:
            ans += 1
print(ans)