split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
S = input()
SLEN = len(S)

memo = [[-1] * 26 for _ in range(SLEN + 1)]

for i in range(SLEN - 1, -1, -1):
    sidx = ord(S[i]) - 97
    for j in range(26):
        memo[i][j] = i if sidx == j else memo[i + 1][j]

ans = []
nextpos = 0
while len(ans) < K:
    for v in memo[nextpos]:
        if -1 < v <= N - (K - len(ans)):
            ans.append(S[v])
            nextpos = v + 1
            break

print("".join(ans))