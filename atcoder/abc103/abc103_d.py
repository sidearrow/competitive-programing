split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
A = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = split_int_input()
    A[a].append(b)
    A[b].append(a)

ans = 0
l = 1
for i in range(2, N + 1):
    for j in A[i]:
        if j >= i:
            continue
        if j >= l:
            l = i
            ans += 1
            break

print(ans)