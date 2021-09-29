import sys

readline = sys.stdin.readline
readline_split_int = lambda: [int(v) for v in readline().split()]

N, M = readline_split_int()
AB = [readline_split_int() for _ in range(M)]
K = int(readline())
CD = [readline_split_int() for _ in range(K)]


def count(bit):
    s = set()
    for i in range(K):
        s.add(CD[i][bit >> i & 1])
    cnt = 0
    for a, b in AB:
        if a in s and b in s:
            cnt += 1
    return cnt


ans = 0
for bit in range(2 ** K):
    cnt = count(bit)
    ans = max(ans, cnt)

print(ans)