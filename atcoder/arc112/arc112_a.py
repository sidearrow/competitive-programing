T = int(input())


def solve(l, r):
    tmp = (r - l) - l + 1
    if tmp < 0:
        return 0
    return (tmp + 1) * tmp // 2


for _ in range(T):
    l, r = [int(v) for v in input().split()]
    print(solve(l, r))