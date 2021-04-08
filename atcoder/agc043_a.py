split_int_input = lambda: [int(v) for v in input().split()]
H, W = split_int_input()
S = [[v == "#" for v in input()] for _ in range(H)]
ans = [[0] * W for _ in range(H)]

ans[0][0] = 1 if S[0][0] else 0
for i in range(1, H):
    ans[i][0] = ans[i - 1][0]
    if not S[i - 1][0] and S[i][0]:
        ans[i][0] += 1
for i in range(1, W):
    ans[0][i] = ans[0][i - 1]
    if not S[0][i - 1] and S[0][i]:
        ans[0][i] += 1

for i in range(1, H):
    for j in range(1, W):
        h = ans[i - 1][j]
        if not S[i - 1][j] and S[i][j]:
            h += 1
        w = ans[i][j - 1]
        if not S[i][j - 1] and S[i][j]:
            w += 1
        ans[i][j] = min(h, w)

print(ans[H - 1][W - 1])
