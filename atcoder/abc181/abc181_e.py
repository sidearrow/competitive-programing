from bisect import bisect_left

input_split_int = lambda: [int(v) for v in input().split()]

N, M = input_split_int()
H = input_split_int()
W = input_split_int()

H.sort()

h0 = []
tmp = 0
for i in range(0, N - 1, 2):
    tmp += H[i + 1] - H[i]
    h0.append(tmp)
h1 = []
tmp = 0
for i in range(1, N - 1, 2):
    tmp += H[i + 1] - H[i]
    h1.append(tmp)

ans = float("inf")
for w in W:
    idx = bisect_left(H, w)
    if idx % 2 == 1 or idx == N:
        idx -= 1
    tmp = abs(w - H[idx])
    if len(h1) > 0:
        tmp += h1[-1]
    if idx > 0:
        tmp = tmp + h0[idx // 2 - 1] - h1[idx // 2 - 1]
    ans = min(ans, tmp)
print(ans)