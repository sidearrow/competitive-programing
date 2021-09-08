split_int_input = lambda: [int(v) for v in input().split()]

N, M, Q = split_int_input()
A = [[0] * N for _ in range(N)]
for _ in range(M):
    l, r = split_int_input()
    A[l - 1][r - 1] += 1
for i in range(N):
    for j in range(1, N):
        A[i][j] += A[i][j - 1]
for _ in range(Q):
    l, r = split_int_input()
    ans = 0
    for i in range(l - 1, r):
        ans += A[i][r - 1]
    print(ans)