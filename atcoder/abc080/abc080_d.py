import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, C = readline2()
STC = [readline2() for _ in range(N)]
STC.sort(key=lambda v: v[0])

memo = []
ans = 0
for s, t, c in STC:
    is_append = True
    for i in range(len(memo)):
        _t, _c = memo[i]
        if (c == _c and _t <= s) or (c != _c and _t <= s - 0.5):
            memo[i] = [t, c]
            is_append = False
            break
    if is_append:
        memo.append([t, c])
    ans = max(ans, len(memo))

print(ans)