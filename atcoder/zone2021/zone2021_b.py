split_int_input = lambda: [int(v) for v in input().split()]

N, D, H = split_int_input()

ans = 0
for _ in range(N):
    d, h = split_int_input()
    tmp = (D * h - d * H) / (D - d)
    ans = max(ans, tmp)

print(ans)