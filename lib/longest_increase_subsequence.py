# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D

from bisect import bisect_left


def lis(a: list):
    res = [a[0]]
    for v in a[1:]:
        if v > res[-1]:
            res.append(v)
        else:
            res[bisect_left(res, v)] = v
    return len(res)
