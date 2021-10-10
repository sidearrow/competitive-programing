import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, P = readline2()
A = readline2()

ans = 0
for a in A:
    if a < P:
        ans += 1

print(ans)