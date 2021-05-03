split_int_input = lambda: [int(v) for v in input().split()]
N, X, Y = split_int_input()
X -= 1
Y -= 1

ans = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        tmp = min(j - i, abs(X - i) + 1 + abs(Y - j))
        ans[tmp] += 1

for v in ans[1:]:
    print(v)