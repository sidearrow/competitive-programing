split_int_input = lambda: [int(v) for v in input().split()]
N, K = split_int_input()

ans = 0
for b in range(K + 1, N + 1):
    # print(ans)
    ans += N // b * (b - K)
    mod = N % b
    if mod >= K:
        ans += mod - K + 1
        if K == 0:
            ans -= 1

print(ans)