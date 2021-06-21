import sys

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

N, K = split_int_readline()

if N == 1:
    print(K)
elif N == 2:
    print(K * (K - 1))
else:
    mod = 10 ** 9 + 7
    ans = pow(K - 2, N - 2, mod) * K * (K - 1) % mod
    print(ans)
