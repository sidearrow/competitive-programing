split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
A = split_int_input()

for _ in range(K):
    memo = [0] * N
    for i, a in enumerate(A):
        l = max(0, i - a)
        r = min(N, i + a + 1)
        memo[l] += 1
        if r < N:
            memo[r] -= 1

    no_update = True
    for i in range(1, N):
        memo[i] += memo[i - 1]
        if memo[i] != N:
            no_update = False
    if memo[0] == N and no_update:
        ans = [N] * N
        print(*ans)
        exit()
    A = memo

print(*A)