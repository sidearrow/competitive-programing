N = int(input())

res = 0
for i in range(1, N):
    res += (N - 1) // i

print(res)
