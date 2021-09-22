input_split_int = lambda: [int(v) for v in input().split()]

MAX = 5000 + 1
N, K = input_split_int()
A = [[0] * MAX for _ in range(MAX)]
for _ in range(N):
    a, b = input_split_int()
    A[a][b] += 1

for i in range(MAX):
    for j in range(1, MAX):
        A[i][j] += A[i][j - 1]
for i in range(MAX):
    for j in range(1, MAX):
        A[j][i] += A[j - 1][i]

ans = -1
for i in range(1, MAX - K):
    for j in range(1, MAX - K):
        i1 = i - 1
        i2 = i + K
        j1 = j - 1
        j2 = j + K
        tmp = A[i2][j2] - A[i1][j2] - A[i2][j1] + A[i1][j1]
        if tmp > ans:
            ans = tmp

print(ans)
