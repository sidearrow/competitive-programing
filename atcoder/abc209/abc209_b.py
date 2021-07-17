import sys

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

N, X = split_int_readline()
A = split_int_readline()

tmp = 0
for i, a in enumerate(A, 1):
    if i % 2 == 0:
        tmp += a - 1
    else:
        tmp += a

if X >= tmp:
    print("Yes")
else:
    print("No")