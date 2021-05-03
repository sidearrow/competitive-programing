N = int(input())
res = [-1] * N
for i in range(0, N-1):
    u, v, w = map(int, input().split())
    if w % 2 == 0:
        if res[u-1] != -1 and res[v-1] == -1:
            res[v-1] = res[u-1]
        elif res[v-1] != -1 and res[u-1] == -1:
            res[u-1] = res[v-1]
        elif res[u-1] == -1 and res[v-1] == -1:
            res[u-1] = 0
            res[v-1] = 0
    else:
        if res[u-1] != -1 and res[v-1] == -1:
            if res[u-1] == 0:
                res[v-1] = 1
            else:
                res[v-1] = 0
        elif res[v-1] != -1 and res[u-1] == -1:
            if res[v-1] == 0:
                res[u-1] = 1
            else:
                res[u-1] = 0
        elif res[u-1] == -1 and res[v-1] == -1:
            res[u-1] = 0
            res[v-1] = 1

for i in res:
    print(i)
