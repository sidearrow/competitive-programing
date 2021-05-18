split_int_input = lambda: [int(v) for v in input().split()]

N, M, D = split_int_input()

if D == 0:
    ans = 1 / N * (M - 1)
else:
    ans = (N - D) * 2 / (N * N) * (M - 1)

print(ans)