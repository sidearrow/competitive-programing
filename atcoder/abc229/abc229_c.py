import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N,W = readline2()
AB = [readline2() for _ in range(N)]
AB.sort(key=lambda v: v[0], reverse=True)

w = W
ans = 0
for a, b in AB:
    if w <= b:
        ans += a * w
        break
    ans += a * b
    w -= b

print(ans)
