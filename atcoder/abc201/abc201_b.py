split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = []
for _ in range(N):
    s, t = input().split()
    t = int(t)
    A.append([s, t])

A = sorted(A, key=lambda v: v[1], reverse=True)

print(A[1][0])