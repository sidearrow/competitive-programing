split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()

tmp = min(N, M // 2)
M -= tmp * 2
ans = tmp + M // 4

print(ans)
