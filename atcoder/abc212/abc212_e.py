split_int_input = lambda: [int(v) for v in input().split()]

MOD = 998244353
N, M, K = split_int_input()
A = [[] for _ in range(N)]

for _ in range(M):
    u, v = split_int_input()
    A[u - 1].append(v - 1)
    A[v - 1].append(u - 1)

memo = [0] * N
memo[0] = 1
memosum = 1
for _ in range(K - 1):
    newmemo = [0] * N
    newmemosum = 0
    for i in range(N):
        tmp = memosum - memo[i]
        for j in A[i]:
            tmp -= memo[j]
        tmp %= MOD
        newmemo[i] = tmp
        newmemosum = (newmemosum + tmp) % MOD
    memo = newmemo
    memosum = newmemosum

ans = 0
for i in range(N):
    ans = (ans + memo[i]) % MOD
ans = (ans - memo[0]) % MOD
for i in A[0]:
    ans = (ans - memo[i]) % MOD

print(ans)