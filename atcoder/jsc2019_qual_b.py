split_int_input = lambda: [int(v) for v in input().split()]
N, K = split_int_input()
A = split_int_input()

cntk = 0
cntk1 = 0
for i, a1 in enumerate(A):
    for j, a2 in enumerate(A):
        if a1 > a2:
            if i < j:
                cntk += 1
            else:
                cntk1 += 1

mod = 10 ** 9 + 7
ans = cntk * ((1 + K) * K // 2) % mod
ans += cntk1 * (K * (K - 1) // 2) % mod
ans %= mod
print(ans)
