N = int(input())
P = [int(input()) for _ in range(N)]

memo = {}
for p in P:
    if p - 1 in memo:
        memo[p] = memo[p - 1] + 1
    else:
        memo[p] = 1

l = 0
for v in memo.values():
    if v > l:
        l = v

print(N - l)
