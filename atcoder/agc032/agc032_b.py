N = int(input())

tmp = N if N % 2 else N + 1
ans = []
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if i != j and i + j != tmp:
            ans.append([i, j])

print(len(ans))
for v in ans:
    print(*v)