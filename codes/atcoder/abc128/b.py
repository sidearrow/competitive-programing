N = int(input())
S = []
P = []
res = [-1]*N
for i in range(N):
    tmp = input().split()
    S.append(tmp[0])
    P.append(int(tmp[1]))
    this = 1
    for j in range(i):
        if S[i] < S[j]:
            res[j] += 1
            continue
        if S[i] == S[j]:
            if P[i] > P[j]:
                res[j] += 1
                continue
        this += 1
    res[i] = this
ans = [-1]*N
for i, v in enumerate(res):
    ans[v-1] = i + 1
for v in ans:
    print(v)
