import sys

readline = sys.stdin.readline
readline_split_int = lambda: [int(v) for v in readline().split()]


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
N, K = readline_split_int()
A = readline_split_int()
A.sort()

comb = Combination(N, MOD)

mn = 0
mx = 0
for i in range(N):
    if N - i >= K:
        mn += A[i] * comb.get(N - i - 1, K - 1)
        mn %= MOD
    if i + 1 >= K:
        mx += A[i] * comb.get(i, K - 1)
        mx %= MOD

ans = (mx - mn) % MOD
print(ans)
