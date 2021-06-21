import sys

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

N, Q = split_int_readline()
A = split_int_readline()

e = 0
D = [0] * N
for i in range(1, N):
    d = A[i] - A[i - 1]
    D[i] = d
    e += abs(d)

for _ in range(Q):
    l, r, v = split_int_readline()
    if l > 1:
        prev = D[l - 1]
        D[l - 1] += v
        e += abs(D[l - 1]) - abs(prev)
    if r < N:
        prev = D[r]
        D[r] -= v
        e += abs(D[r]) - abs(prev)
    print(e)
