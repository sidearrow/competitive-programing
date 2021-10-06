from collections import Counter

N = int(input())
S = [int(input()) for _ in range(N)]
Q = int(input())
K = [int(input()) for _ in range(Q)]

S = [s for s in S if s > 0]

memo = [0] * (N + 1)
uniq_s = sorted(set(S), reverse=True)
cont_s = Counter(S)
tmp = 0
for s in uniq_s:
    s_num = cont_s[s]
    for i in range(s_num):
        memo[tmp] = s + 1
        tmp += 1

for k in K:
    print(memo[k])