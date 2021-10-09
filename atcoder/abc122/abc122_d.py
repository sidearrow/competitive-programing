MOD = 10 ** 9 + 7
N = int(input())

A, C, G, T = list(range(1, 5))
memo = [0] * 125
memo[0] = 1

AG = A * 5 + G  # C
GA = G * 5 + A  # C
AC = A * 5 + C  # G

for _ in range(N):
    new_memo = [0] * 125
    for i in range(125):
        imod25 = i % 25
        base = imod25 * 5
        for j in range(1, 5):
            if imod25 == AG and j == C:
                continue
            if imod25 == GA and j == C:
                continue
            if imod25 == AC and j == G:
                continue
            if i % 5 == G and i // 25 == A and j == C:
                continue
            if i // 5 == AG and j == C:
                continue
            new_memo[base + j] += memo[i]
            new_memo[base + j] %= MOD
    memo = new_memo


ans = sum(memo) % MOD
print(ans)