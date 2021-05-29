split_int_input = lambda: [int(v) for v in input().split()]

N, L = split_int_input()
memo = [0] * (N + 1)
memo[0] = 1
mod = 10 ** 9 + 7
for i in range(1, N + 1):
    tmp = memo[i - 1]
    if i - L >= 0:
        tmp += memo[i - L]
    memo[i] = tmp % mod

print(memo[-1])