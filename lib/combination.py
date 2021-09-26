"""
階乗 factorial
"""


# 前処理あり
class Combination:
    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.inv[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n - 1, -1, -1):
            self.inv[i] = self.inv[i + 1] * (i + 1) % self.mod

    def get(self, n, r):
        return self.fac[n] * self.inv[n - r] * self.inv[r] % self.mod


MOD = 10 ** 9 + 7
comb = Combination(100, MOD)
assert comb.get(100, 3) == (100 * 99 * 98) // (3 * 2 * 1)


# 前処理なし
def _comb(n, r, mod):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * pow(i + 1, mod - 2, mod) % mod
    return res


def _comb(n, k):
    res = 1
    for i in range(k):
        res = res * (n - i) // (i + 1)
    return res
