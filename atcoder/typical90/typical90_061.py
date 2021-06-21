import sys
from collections import deque

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

Q = int(readline())
dq = deque()

for _ in range(Q):
    t, x = split_int_readline()
    if t == 1:
        dq.appendleft(x)
    elif t == 2:
        dq.append(x)
    else:
        print(dq[x - 1])
