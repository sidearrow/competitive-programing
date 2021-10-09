import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N, K = readline2()
A = readline2()

memo = [0] * 50
for a in A:
    dig = 0
    while a > 0:
        if a & 1:
            memo[dig] += 1
        a >>= 1
        dig += 1

ans = 0
flg = False
for i in range(49, -1, -1):
    n0, n1 = N - memo[i], memo[i]
    _ans = 0
    if K >> i & 1:
        if n0 >= n1:
            _ans += n0
        else:
            _ans += n1
            flg = True
    else:
        if n1 >= n0:
            _ans += n1
        else:
            _ans += n0 if flg else n1
    ans += _ans * (1 << i)

print(ans)