split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
A = [split_int_input() for _ in range(H)]

row = [0] * H
col = [0] * W
for h in range(H):
    for w in range(W):
        a = A[h][w]
        row[h] += a
        col[w] += a

ans = [[0] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        ans[h][w] = row[h] + col[w] - A[h][w]

for row in ans:
    print(*row)