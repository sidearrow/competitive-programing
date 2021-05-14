import sys

input = sys.stdin.readline
split_int_input = lambda: [int(v) for v in input().split()]

H, W, M = split_int_input()
r = [0] * (H + 1)
c = [0] * (W + 1)
bombs = []
for _ in range(M):
    h, w = split_int_input()
    bombs.append([h, w])
    r[h] += 1
    c[w] += 1

maxr = max(r)
maxrn = sum(1 for v in r if v == maxr)
maxc = max(c)
maxcn = sum(1 for v in c if v == maxc)

tmp = 0
for h, w in bombs:
    if r[h] == maxr and c[w] == maxc:
        tmp += 1

if tmp == maxrn * maxcn:
    print(maxr + maxc - 1)
else:
    print(maxr + maxc)