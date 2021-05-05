split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
c = [0] * (N + 1)
for i in range(2, N + 1):
    if c[i] > 0:
        continue
    for j in range(i, N + 1, i):
        c[j] += 1

ans = 0
for v in c:
    if v >= K:
        ans += 1
print(ans)