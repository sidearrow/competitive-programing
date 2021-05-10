split_int_input = lambda: [int(v) for v in input().split()]

T, N = split_int_input()

memo = [False] * (100 + T)
for i in range(0, 100):
    a = (100 + T) * i // 100
    memo[a] = True

memo = [i for i, v in enumerate(memo) if not v]
n_div, n_mod = divmod(N, len(memo))
if n_mod == 0:
    ans = (n_div - 1) * (100 + T) + memo[-1]
else:
    ans = n_div * (100 + T) + memo[n_mod - 1]

print(ans)