import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, D = readline2()
LR = [readline2() for _ in range(N)]
LR.sort(key=lambda v: v[1])

r2 = 0
ans = 0
for l, r in LR:
    if l > r2:
        ans += 1
        r2 = r + D - 1

print(ans)