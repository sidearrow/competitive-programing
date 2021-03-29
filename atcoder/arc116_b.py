import sys

input = sys.stdin.readline
MOD = 998244353

split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = split_int_input()
A.sort(reverse=True)

ans = A[0] ** 2 % MOD
if N == 1:
    print(ans)
    exit()

ans += A[1] ** 2 + A[0] * A[1]
ans %= MOD
if N == 2:
    print(ans)
    exit()

tmp = A[0] + A[1]
prev = A[1]
for t in A[2:]:
    tmp = ((tmp - prev) * 2 + prev + t) % MOD
    ans += tmp * t
    ans %= MOD
    prev = t

print(ans)