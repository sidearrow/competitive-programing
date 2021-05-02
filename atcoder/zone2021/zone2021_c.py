import itertools

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = [split_int_input() for _ in range(N)]


def convert(a, n):
    res = 0
    for v in a:
        res <<= 1
        if v >= n:
            res += 1
    return res


def check(n):
    patterns = set()
    for a in A:
        patterns.add(convert(a, n))
    for comb in itertools.product(patterns, repeat=3):
        if comb[0] | comb[1] | comb[2] == 31:
            return True
    return False


l = 0
r = 10 ** 9 + 10
while l + 1 < r:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid

print(l)