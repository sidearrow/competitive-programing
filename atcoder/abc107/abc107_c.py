split_int_input = lambda: [int(v) for v in input().split()]
N, K = split_int_input()
x = split_int_input()

ans = 10 ** 15
for i in range(N):
    if i + K > N:
        break
    r = i + K - 1
    if x[i] <= 0 and x[r] <= 0:
        ans = min(ans, abs(x[i]))
        continue
    if x[i] >= 0 and x[r] >= 0:
        ans = min(ans, abs(x[r]))
        continue
    ans = min(
        ans,
        min(
            abs(x[i]) * 2 + x[r],
            abs(x[i]) + x[r] * 2,
        ),
    )

print(ans)