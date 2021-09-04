from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()

memo = [[] for _ in range(N)]
top = [0] * N
tt = []
for i in range(M):
    k = int(input())
    a = split_int_input()
    for j in range(k):
        a[j] -= 1
        memo[a[j]].append(i)
    top[a[0]] += 1
    a = deque(a)
    a.popleft()
    tt.append(a)

dq = deque()
for i in range(N):
    if top[i] == 2:
        dq.append(i)

cnt = 0
while len(dq) > 0:
    cnt += 1
    a = dq.popleft()
    for ttidx in memo[a]:
        if len(tt[ttidx]) > 0:
            na = tt[ttidx].popleft()
            top[na] += 1
            if top[na] == 2:
                dq.append(na)

print("Yes" if cnt == N else "No")