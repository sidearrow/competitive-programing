import itertools

split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = split_int_input()
    G[a].append(b)
    G[b].append(a)

ans = 0
l = N - 2 + 1
for vs in itertools.permutations(range(2, N + 1)):
    valid = True
    for i, v in enumerate(vs):
        frm = 1 if i == 0 else vs[i - 1]
        if v not in G[frm]:
            valid = False
            break
    if valid:
        ans += 1

print(ans)