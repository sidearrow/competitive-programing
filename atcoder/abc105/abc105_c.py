N = int(input())

l = 0
r = 1
base = 1
memo = []
while not (l <= N <= r):
    base *= -2
    if base < 0:
        _l = l
        l += base
        memo.append([base, l, _l - 1])
    else:
        _r = r
        r += base
        memo.append([base, _r + 1, r])
memo = reversed(memo)
ans = []
for base, l, r in memo:
    if l <= N <= r:
        N -= base
        ans.append(1)
    else:
        ans.append(0)
ans.append(N)

print(*ans, sep="")
