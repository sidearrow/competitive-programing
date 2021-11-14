import sys

_rl = sys.stdin.readline

N = int(_rl())
MAX = 10 ** 7
ans = 0
for i in range(1, MAX):
    if i * i * i > N:
        break
    for j in range(i, MAX):
        k = N // (i * j)
        if k < j:
            break
        ans += k - j + 1

print(ans)
