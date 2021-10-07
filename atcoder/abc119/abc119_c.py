import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, *ABC = readline2()
L = [int(readline()) for _ in range(N)]

ans = float("inf")
for i in range(4 ** N):
    memo = [0, 0, 0]
    mp = 0
    for j in range(N):
        if i % 4 > 0:
            _i = i % 4 - 1
            if memo[_i] != 0:
                mp += 10
            memo[_i] += L[j]
        i //= 4
    memo.sort(reverse=True)
    if memo[-1] == 0:
        continue
    for j in range(3):
        mp += abs(ABC[j] - memo[j])
    if mp < ans:
        ans = mp

print(ans)