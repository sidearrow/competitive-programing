split_int_input = lambda: [int(v) for v in input().split()]
N, M = split_int_input()
A = split_int_input()

cnt = [0] * (max(A) + 2)
for i in range(M):
    cnt[A[i]] += 1

ans = 0
for i, c in enumerate(cnt):
    if c == 0:
        ans = i
        break

for i in range(N - M):
    l = A[i]
    r = A[i + M]
    cnt[l] -= 1
    cnt[r] += 1
    if cnt[l] == 0:
        ans = min(ans, l)

print(ans)