split_int_input = lambda: [int(v) for v in input().split()]
N, M = split_int_input()

ans = 1
for i in range(1, int(M ** 0.5) + 1):
    if M % i == 0:
        if i >= N:
            ans = max(ans, M // i)
        if M // i >= N:
            ans = max(ans, i)

print(ans)