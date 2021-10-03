N = int(input())


def get_digs(n):
    res = []
    while n > 0:
        d, m = divmod(n, 10)
        res.append(m)
        n = d
    return res


def join_digs(digs):
    n = 0
    for i in range(len(digs)):
        n *= 10
        n += digs[i]
    return n


digs = get_digs(N)
dignum = len(digs)

ans = -1
for bit in range(1 << dignum):
    a = []
    b = []
    for i in range(dignum):
        if bit >> i & 1:
            a.append(digs[i])
        else:
            b.append(digs[i])
    a.sort(reverse=True)
    b.sort(reverse=True)
    if len(a) == 0 or len(b) == 0 or a[0] == 0 or b[0] == 0:
        continue
    tmp_ans = join_digs(a) * join_digs(b)
    if tmp_ans > ans:
        ans = tmp_ans

print(ans)
