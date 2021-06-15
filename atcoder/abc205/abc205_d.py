import sys
import bisect

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

N, Q = split_int_readline()
A = split_int_readline()

idx = []
orig = []
for i in range(N):
    if i + 1 < N and A[i] + 1 == A[i + 1]:
        continue
    orig.append(A[i] + 1)
    idx.append(A[i] - i)

for _ in range(Q):
    k = int(input())
    i = bisect.bisect_right(idx, k)
    if i == 0:
        print(k)
    else:
        ans = orig[i - 1] + (k - idx[i - 1])
        print(ans)
