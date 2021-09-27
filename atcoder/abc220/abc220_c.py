input_split_int = lambda: [int(v) for v in input().split()]

N = int(input())
A = input_split_int()
X = int(input())

asum = sum(A)
d, m = divmod(X, asum)

ans = d * N
i = 0
while m >= 0:
    m -= A[i]
    i += 1
    ans += 1

print(ans)