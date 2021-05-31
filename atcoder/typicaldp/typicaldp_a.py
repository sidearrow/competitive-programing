import sys

readline = sys.stdin.readline

N = int(readline())
P = [int(v) for v in readline().split()]

st_score = set([0])
for p in P:
    tmp = set()
    for v in st_score:
        tmp.add(v + p)
    for v in tmp:
        st_score.add(v)

ans = len(st_score)
print(ans)