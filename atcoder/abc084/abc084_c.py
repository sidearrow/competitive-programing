import math

split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
C = [0] * (N - 1)
S = [0] * (N - 1)
F = [0] * (N - 1)
for i in range(N - 1):
    C[i], S[i], F[i] = split_int_input()

ans = []
for i in range(N - 1):
    a = 0
    for j in range(i, N - 1):
        b = math.ceil((a - S[j]) / F[j])
        if b < 0:
            b = 0
        a = S[j] + F[j] * b + C[j]
    ans.append(a)
ans.append(0)

for v in ans:
    print(v)