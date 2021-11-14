import sys

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]

N = int(_rl())
AB = [_rl2() for _ in range(N)]

AB.sort(key=lambda v: v[1])
ans = True
t = 0
for a, b in AB:
    t += a
    if t > b:
        ans = False
        break

print("Yes" if ans else "No")
