import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

A = readline2()
A.sort(reverse=True)
print(A[2])