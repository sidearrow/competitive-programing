split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
A = sorted(split_int_input())
B = sorted(split_int_input())
C = sorted(split_int_input())

bc = [0] * (N + 1)
cidx = N
for i in range(N - 1, -1, -1):
    while cidx > 0 and B[i] < C[cidx - 1]:
        cidx -= 1
    bc[i] = bc[i + 1] + N - cidx

ans = 0
bidx = N
for i in range(N - 1, -1, -1):
    while bidx > 0 and A[i] < B[bidx - 1]:
        bidx -= 1
    if bidx < N:
        ans += bc[bidx]

print(ans)
