from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]
N, M = split_int_input()
A = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = split_int_input()
    A[a].append(b)
    A[b].append(a)

q = deque([[1, -1]])
ans = [-1] * (N + 1)
seen = [False] * (N + 1)
while 1:
    if len(q) == 0:
        break
    idx, frm = q.popleft()
    ans[idx] = frm
    for v in A[idx]:
        if seen[v]:
            continue
        seen[v] = True
        q.append([v, idx])
b = True
for i in range(2, N + 1):
    if ans[i] == -1:
        b = False
        break

if b:
    print("Yes")
    for i in range(2, N + 1):
        print(ans[i])
else:
    print("No")