split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
V = split_int_input()


def calc_max_v(k):
    res = 0
    push_n = K - k
    for ln in range(k + 1):
        rn = k - ln
        get_v = []
        for i in range(ln):
            get_v.append(V[i])
        for i in range(rn):
            get_v.append(V[N - i - 1])
        get_v = sorted(get_v)
        idx = 0
        for i in range(min(push_n, len(get_v))):
            if get_v[i] > 0:
                break
            idx += 1
        res = max(res, sum(get_v[idx:]))
    return res


ans = 0
for i in range(1, min(N + 1, K + 1)):
    ans = max(ans, calc_max_v(i))

print(ans)