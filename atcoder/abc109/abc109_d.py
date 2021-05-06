split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
A = [split_int_input() for _ in range(H)]

prev = None
ans = []
for i in range(H):
    rng = range(W)
    if i % 2:
        rng = reversed(rng)
    for j in rng:
        if prev is not None:
            ans.append([*prev, i + 1, j + 1])
            A[i][j] += 1
        if A[i][j] % 2:
            prev = [i + 1, j + 1]
            A[i][j] -= 1
        else:
            prev = None

print(len(ans))
for v in ans:
    print(*v)