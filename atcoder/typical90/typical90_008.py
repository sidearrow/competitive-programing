N = int(input())
S = input()

tmp = [0] * 7
mod = 10 ** 9 + 7
for s in S:
    for i, a in enumerate("atcoder"):
        if s == a:
            if i == 0:
                tmp[0] += 1
            else:
                tmp[i] = (tmp[i] + tmp[i - 1]) % mod

print(tmp[-1])