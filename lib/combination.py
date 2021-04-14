"""
階乗 factorial
"""


# 前処理あり
class Combination:
    def __init__(self, n, mod):
        self.mod = mod
        self.fact = [0] * (n + 1)
        self.finv = [0] * (n + 1)
        inv = [0] * (n + 1)

        self.fact[0] = self.fact[1] = 1
        self.finv[0] = self.finv[1] = 1
        inv[1] = 1

        for i in range(2, n + 1):
            inv[i] = self.mod - inv[self.mod % i] * (self.mod // i) % self.mod
            self.fact[i] = self.fact[i - 1] * i % self.mod
            self.finv[i] = self.finv[i - 1] * inv[i] % self.mod
        print(self.fact, self.finv, inv)

    def get(self, n, r):
        return self.fact[r] * (self.finv[r] * self.finv[n - r] % self.mod) % self.mod


# 前処理なし
def comb(n, r, mod):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * pow(i + 1, mod - 2, mod) % mod
    return res
