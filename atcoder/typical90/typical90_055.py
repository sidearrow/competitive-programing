import sys
import itertools

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

N, P, Q = split_int_readline()
A = [v % P for v in split_int_readline()]

ans = 0
for c in itertools.combinations(A, 5):
    if (c[0] * c[1] * c[2] * c[3] * c[4]) % P == Q:
        ans += 1

print(ans)