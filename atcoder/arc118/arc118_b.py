split_int_input = lambda: [int(v) for v in input().split()]

K, N, M = split_int_input()
A = split_int_input()

ans = []
mod = []
for i, a in enumerate(A):
    d, m = divmod(a * M, N)
    ans.append(d)
    mod.append([i, m])

mod = sorted(mod, key=lambda v: v[1], reverse=True)

for i in range(M - sum(ans)):
    ans[mod[i][0]] += 1

print(*ans)