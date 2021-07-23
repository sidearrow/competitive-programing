split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
MOD = 10 ** 5

next_num = [-1] * (10 ** 5 + 1)
num_list = []
num_idx = [-1] * (10 ** 5 + 1)

n = N
idx_cnt = 0
while next_num[n] == -1:
    tmp = n
    _n = n
    while _n > 0:
        d, m = divmod(_n, 10)
        tmp += m
        _n = d
    tmp %= MOD
    next_num[n] = tmp
    num_list.append(tmp)
    num_idx[n] = idx_cnt
    n = tmp
    idx_cnt += 1

lnl = len(num_list)
if K <= lnl:
    print(num_list[K - 1])
    exit()

lidx = num_idx[n]
loopn = lnl - lidx
ansidx = (K - lnl) % loopn + lidx - 1
print(num_list[ansidx])