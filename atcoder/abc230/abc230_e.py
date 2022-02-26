import sys

readline = sys.stdin.readline

N = int(readline())
nl = int(N ** 0.5)
nr = N // (nl + 1)

ans = 0
r = N
for i in range(1, nr + 1):
    l = N // (i + 1)
    ans += (r - l) * i
    r = l

for i in range(1, nl + 1):
    ans += N // i

print(ans)