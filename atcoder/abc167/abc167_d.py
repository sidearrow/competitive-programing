from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
A = [int(v) - 1 for v in input().split()]

seen = [False] * N
i = A[0]
dq = deque()
while 1:
    dq.append(i)
    if seen[i]:
        break
    seen[i] = True
    i = A[i]

a = dq.pop()
b = -1
loop = deque()
while a != b:
    b = dq.pop()
    loop.appendleft(b)

if K <= len(dq):
    print(dq[K - 1] + 1)
else:
    K -= len(dq)
    print(loop[K % len(loop) - 1] + 1)
