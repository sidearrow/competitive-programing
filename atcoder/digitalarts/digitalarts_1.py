S = input().split()
N = int(input())
T = [input() for _ in range(N)]


def check(a, b):
    if len(a) != len(b):
        return False
    res = True
    for c, d in zip(a, b):
        if d == "*":
            continue
        if c != d:
            res = False
            break
    return res


ans = []
for s in S:
    res = False
    for t in T:
        if check(s, t):
            ans.append("*" * len(s))
            res = True
            break
    if not res:
        ans.append(s)

print(*ans)