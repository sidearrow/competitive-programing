input_split_int = lambda: [int(v) for v in input().split()]

N, M = input_split_int()
A = input_split_int()
R = [[] for _ in range(N)]

for _ in range(M):
    x, y = input_split_int()
    R[y - 1].append(x - 1)

mx = -1 * (10 ** 9 + 10)
a = [*A]
for i in range(N):
    if len(R[i]) == 0:
        continue
    tmp = min([a[x] for x in R[i]])
    mx = max(mx, A[i] - tmp)
    a[i] = min(a[i], tmp)

print(mx)
