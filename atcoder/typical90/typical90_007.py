import bisect

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()
Q = int(input())

A = sorted(A)

for _ in range(Q):
    b = int(input())
    idx = bisect.bisect_left(A, b)
    if idx == 0:
        print(abs(A[0] - b))
    elif idx == N:
        print(abs(A[-1] - b))
    else:
        print(min(abs(A[idx - 1] - b), abs(A[idx] - b)))
