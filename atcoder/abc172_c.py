import bisect

split_int_input = lambda: [int(v) for v in input().split()]
N, M, K = split_int_input()
A = split_int_input()
B = split_int_input()

a = [0]
tmp = 0
for _a in A:
    tmp += _a
    a.append(tmp)

b = [0]
tmp = 0
for _b in B:
    tmp += _b
    b.append(tmp)

tmpbn = M
ans = 0
for an in range(N + 1):
    for bn in range(tmpbn, -1, -1):
        if a[an] + b[bn] <= K:
            ans = max(ans, an + bn)
            tmpbn = bn
            break

print(ans)
