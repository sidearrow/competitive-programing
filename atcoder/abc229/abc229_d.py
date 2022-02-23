import sys
from collections import deque

readline = sys.stdin.readline

S = readline().strip()
K = int(readline())
SL = len(S)


dq = deque()
ans = -1
for i, v in enumerate(s):
    dq.append(i)
    while len(dq) > 0 and (v - s[dq[0]]) > K:
        dq.popleft()
    print(dq)
    ans = max(ans, dq[-1] - dq[0] + 1)

print(ans)