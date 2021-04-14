split_int_input = lambda: [int(v) for v in input().split()]
n, a, b = split_int_input()


def comb(n, r, mod):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * pow(i + 1, mod - 2, mod) % mod
    return res


mod = 10 ** 9 + 7
ans = pow(2, n, mod) - comb(n, a, mod) - comb(n, b, mod) - 1
ans %= mod

print(ans)