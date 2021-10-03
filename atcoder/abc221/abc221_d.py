import sys

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]


class Compress:
    def __init__(self, l):
        self.uniq = sorted(set(l))
        self.cmp = {k: i for i, k in enumerate(self.uniq)}

    def idx(self, n):
        return self.cmp[n]

    def orig(self, idx):
        return self.uniq[idx]


N = int(_rl())
AB = []
days = []
for _ in range(N):
    a, b = _rl2()
    b += a
    AB.append([a, b])
    days.append(a)
    days.append(b)

cmpdays = Compress(days)
memo = [0] * (len(cmpdays.uniq))
for a, b in AB:
    a, b = cmpdays.idx(a), cmpdays.idx(b)
    memo[a] += 1
    memo[b] -= 1

for i in range(1, len(memo)):
    memo[i] += memo[i - 1]

ans = [0] * N
for i in range(len(memo) - 1):
    un = memo[i]
    if un == 0:
        continue
    dn = cmpdays.orig(i + 1) - cmpdays.orig(i)
    ans[un - 1] += dn

print(*ans)
