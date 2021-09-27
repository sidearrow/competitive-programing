input_split_int = lambda: [int(v) for v in input().split()]

MOD = 998244353
N = int(input())
A = input_split_int()

dp = [0] * 10
dp[A[0]] = 1

for i in range(1, N):
    newdp = [0] * 10
    a = A[i]
    for j in range(10):
        newdp[(a + j) % 10] = (newdp[(a + j) % 10] + dp[j]) % MOD
        newdp[(a * j) % 10] = (newdp[(a * j) % 10] + dp[j]) % MOD
    dp = newdp

for v in dp:
    print(v)
