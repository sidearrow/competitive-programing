import sys
from math import floor

input = sys.stdin.readline


def main():
    N = int(input())
    res = None
    for _ in range(N):
        a, p, x = map(int, input().split())
        if x - floor(a + 0.5) > 0:
            if res is None:
                res = p
            else:
                res = min(res, p)
    print(-1 if res is None else res)


main()