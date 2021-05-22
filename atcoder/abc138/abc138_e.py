import bisect

S = input()
T = input()

s_memo = {}
for i, s in enumerate(S):
    if s not in s_memo:
        s_memo[s] = []
    s_memo[s].append(i)

a = 0
b = 0
for t in T:
    if t not in s_memo:
        print(-1)
        exit()
    idx = bisect.bisect_left(s_memo[t], b)
    if idx < len(s_memo[t]):
        b = s_memo[t][idx] + 1
    else:
        a += 1
        b = s_memo[t][0] + 1

ans = len(S) * a + b
print(ans)