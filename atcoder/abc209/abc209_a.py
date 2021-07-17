import sys

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

A, B = split_int_readline()
print(max(B - A + 1, 0))