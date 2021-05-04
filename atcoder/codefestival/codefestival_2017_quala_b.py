split_int_input = lambda: [int(v) for v in input().split()]
N, M, K = split_int_input()

ans = False
for i in range(N + 1):
    for j in range(M + 1):
        tmp = i * M
        tmp += (N - 2 * i) * j
        if tmp == K:
            ans = True
            break

print("Yes" if ans else "No")