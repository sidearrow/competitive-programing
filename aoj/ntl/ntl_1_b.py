split_int_input = lambda: [int(v) for v in input().split()]
m, n = split_int_input()
mod = 10 ** 9 + 7
ans = pow(m, n, mod)
print(ans)