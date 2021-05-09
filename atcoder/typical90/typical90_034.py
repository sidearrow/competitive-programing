from collections import deque


split_int_input = lambda: [int(v) for v in input().split()]
compress = lambda v: {k: i for i, k in enumerate(sorted(set(v)))}

N, K = split_int_input()
A = split_int_input()
CMP_A = compress(A)

dq = deque()
memo = [0] * N
kind = 0
ans = 0
for a in A:
    a = CMP_A[a]
    dq.append(a)
    if memo[a] == 0:
        kind += 1
    memo[a] += 1
    while kind > K:
        b = dq.popleft()
        memo[b] -= 1
        if memo[b] == 0:
            kind -= 1
    ans = max(ans, len(dq))

print(ans)