S = input()
MOD = 10 ** 9 + 7

m = [0] * 8

for s in S:
    for i, a in enumerate("chokudai"):
        if s == a:
            if i == 0:
                m[i] += 1
            else:
                m[i] = (m[i] + m[i - 1]) % MOD

print(m[-1])