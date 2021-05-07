from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N, X, M = split_int_input()

a = X
dq = deque()
seen = [-1] * (10 ** 5 + 10)
i = 0
while 1:
    if seen[a] > -1:
        break
    seen[a] = i
    dq.append(a)
    a = a * a % M

ans = 0
cnt = N
while cnt > 0:
    if dq[0] != a:
        ans += dq.popleft()
        cnt -= 1
    else:
        len_dq = len(dq)
        ans += (cnt // len_dq) * sum(dq)
        cnt %= len_dq
        a = None

print(ans)