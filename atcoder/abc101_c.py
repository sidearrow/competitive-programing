split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
A = split_int_input()

ans = 0
i = 0
while i < N - 1:
    ans += 1
    i += K - 1

print(ans)