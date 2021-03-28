split_int_input = lambda: [int(v) for v in input().split()]
A, B, N = split_int_input()
x = min(N, B - 1)
ans = A * x // B - A * (x // B)
print(ans)
