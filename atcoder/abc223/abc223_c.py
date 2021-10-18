import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N = int(readline())
AB = []
total = 0
for i in range(N):
    a, b = readline2()
    AB.append([a, b])
    total += a / b
total /= 2

ans = 0
for a, b in AB:
    if a / b < total:
        total -= a / b
        ans += a
    else:
        ans += total * b
        break

print(ans)