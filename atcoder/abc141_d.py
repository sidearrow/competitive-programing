from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]
N, M = split_int_input()
A = deque(sorted(split_int_input(), reverse=True))
dq = deque()
for _ in range(M):
    if len(dq) == 0:
        a = A.popleft()
    else:
        if len(A) == 0 or dq[0] > A[0]:
            a = dq.popleft()
        else:
            a = A.popleft()
    dq.append(a // 2)
ans = sum(A) + sum(dq)
print(ans)