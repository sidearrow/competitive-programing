import sys

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

MOD = 10 ** 9 + 7
N = int(input())
C = sorted(split_int_readline())

ans = 1
for i, c in enumerate(C):
    if c > i:
        ans = ans * (c - i) % MOD
    else:
        print(0)
        exit()
print(ans)