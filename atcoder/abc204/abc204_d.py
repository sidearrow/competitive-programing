import sys

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

N = int(readline())
T = split_int_readline()

s = set([0])
for t in T:
    ns = set(s)
    for v in s:
        ns.add(v + t)
    s = ns

sumt = sum(T)
ans = sumt
for v in s:
    ans = min(ans, max(v, sumt - v))

print(ans)
