import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, M = readline2()
SC = [readline2() for _ in range(M)]


def check(n):
    n = str(n)
    for s, c in SC:
        if len(n) < s or n[s - 1] != str(c):
            return False
    return True


mn = 10 ** (N - 1)
mx = 10 ** N
if N == 1:
    mn = 0
for i in range(mn, mx):
    if check(i):
        print(i)
        exit()
print(-1)