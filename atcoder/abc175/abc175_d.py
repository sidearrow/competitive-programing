import sys

readline = sys.stdin.readline
readline_split_int = lambda: [int(v) for v in readline().split()]

N, K = readline_split_int()
P = [int(v) - 1 for v in readline().split()]
C = readline_split_int()


def check_cycle(cycle):
    csum = sum([C[i] for i in cycle])
    clen = len(cycle)
    ans = -float("inf")
    for i in range(clen):
        sum2 = 0
        for j in range(clen):
            sum2 += C[cycle[(i + j) % clen]]
            tmp = sum2
            if csum > 0:
                tmp = sum2 + csum * ((K - j - 1) // clen)
            if tmp > ans:
                ans = tmp
    return ans


ans = -float("inf")
seen = [False] * N
for i in range(N):
    if not seen[i]:
        seen[i] = True
        cycle = [i]
        nxt = P[i]
        while nxt != i:
            seen[nxt] = True
            cycle.append(nxt)
            nxt = P[nxt]
        _ans = check_cycle(cycle)
        if _ans > ans:
            ans = _ans

print(ans)
