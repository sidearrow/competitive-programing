import sys

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]

N, K = _rl2()
R, S, P = _rl2()
T = _rl().rstrip()

ans = 0
score_map = {"s": R, "p": S, "r": P}
contnum = [0] * K
prev = [""] * K
for i, t in enumerate(T):
    modi = i % K
    if prev[modi] != t:
        contnum[modi] = 1
        ans += score_map[t]
    else:
        contnum[modi] += 1
        if contnum[modi] % 2 == 1:
            ans += score_map[t]
    prev[modi] = t

print(ans)
