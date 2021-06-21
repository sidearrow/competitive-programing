import sys


readline = sys.stdin.readline

N, K = readline().split()
N = [int(n) for n in N]
K = int(K)


def convert(nl):
    b10 = 0
    for n in nl:
        b10 = b10 * 8 + n
    res = []
    while b10 > 0:
        b10, m = divmod(b10, 9)
        if m == 8:
            m = 5
        res.append(m)
    res.reverse()
    return res


n = N
if n == [0]:
    print(0)
    exit()
for _ in range(K):
    n = convert(n)
print(*n, sep="")