S = [int(s) for s in input()]

memo = [0]
tmp = 1
mod = 2019
for s in reversed(S):
    memo.append((s * tmp + memo[-1]) % mod)
    tmp = tmp * 10 % mod
ans = 0
memo2 = [0] * 2019
for a in reversed(memo):
    ans += memo2[a]
    memo2[a] += 1

print(ans)