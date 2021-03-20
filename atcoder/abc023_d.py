import sys

input = sys.stdin.readline


def check(n, h, s, m):
    sec = []
    for i in range(n):
        sec.append((m - h[i]) / s[i])
    sec = sorted(sec)
    res = True
    for i, v in enumerate(sec):
        if i > v:
            res = False
            break
    return res


def main():
    N = int(input())
    H = []
    S = []
    for _ in range(N):
        h, s = [int(v) for v in input().split()]
        H.append(h)
        S.append(s)
    l = 0
    r = 10 ** 15
    while r - l > 1:
        m = (r + l) // 2
        res = check(N, H, S, m)
        if res:
            r = m
        else:
            l = m
    print(r)


main()