N = int(input())
A = [int(v) for v in input().split()]
A.sort(reverse=True)

res = A[0]
for i in range(2, N):
    res += A[i // 2]

print(res)