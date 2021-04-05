from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]
N, M = split_int_input()
A = split_int_input()
BC = []
for _ in range(M):
    b, c = split_int_input()
    BC.append([b, c])

A = deque(sorted(A, reverse=True))
BC = deque(sorted(BC, key=lambda v: v[1], reverse=True))

ans = 0
cnt = 0
while 1:
    if len(BC) == 0 or A[0] >= BC[0][1]:
        ans += A.popleft()
        cnt += 1
    else:
        b, c = BC.popleft()
        a = min(N - cnt, b)
        ans += a * c
        cnt += a
    if cnt == N:
        break

print(ans)