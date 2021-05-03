N, C = [int(v) for v in input().split()]

date = {}
for _ in range(N):
    a, b, c = [int(v) for v in input().split()]
    if a not in date:
        date[a] = 0
    if b + 1 not in date:
        date[b + 1] = 0
    date[a] += c
    date[b + 1] -= c

keys = sorted(list(date.keys()))
tmp_d = 0
tmp_p = 0
res = 0
for k in keys:
    d = k - tmp_d
    if tmp_p > C:
        res += d * C
    else:
        res += d * tmp_p
    tmp_d = k
    tmp_p += date[k]

print(res)