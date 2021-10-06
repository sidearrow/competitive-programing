import sys
from collections import deque

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, K = readline2()
S = [int(readline()) for _ in range(N)]

dq = deque()
k = 1
ans = 0
for s in S:
    if s == 0:
        ans = N
        break
    dq.append(s)
    k *= s
    while len(dq) > 0 and k > K:
        k //= dq.popleft()
    if len(dq) > ans:
        ans = len(dq)

print(ans)