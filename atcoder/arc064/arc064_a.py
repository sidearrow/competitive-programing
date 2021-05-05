split_int_input = lambda: [int(v) for v in input().split()]

N, X = split_int_input()
A = split_int_input()

ans = 0
for i in range(N - 1):
    diff = A[i] + A[i + 1] - X
    if diff > 0:
        ans += diff
        A[i + 1] = max(0, A[i + 1] - diff)

print(ans)