split_int_input = lambda: [int(v) for v in input().split()]
N, P = split_int_input()

ans = P - 1
mod = 10 ** 9 + 7
ans = ans * pow(P - 2, N - 1, mod) % mod

print(ans)