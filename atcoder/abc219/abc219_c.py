X = input()
N = int(input())
S = [input() for _ in range(N)]

x = {}
for i in range(26):
    x[X[i]] = chr(i + 97)

s = []
memo = {}
for v in S:
    tmp = []
    for c in v:
        tmp.append(x[c])
    tmp = "".join(tmp)
    s.append(tmp)
    memo[tmp] = v
s.sort()
for v in s:
    print(memo[v])