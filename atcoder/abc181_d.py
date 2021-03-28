S = input()
s = [0] * 10
slen = len(S)
s[0] = 10
for i in range(slen):
    s[int(S[i])] += 1
ans = False
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            tmps = [*s]
            tmps[i] -= 1
            tmps[j] -= 1
            tmps[k] -= 1
            if slen > 1 and (j == 0):
                continue
            if slen > 2 and (k == 0):
                continue
            if tmps[i] < 0 or tmps[j] < 0 or tmps[k] < 0:
                continue
            if (i + j * 10 + k * 100) % 8 == 0:
                ans = True
                break
        if ans:
            break
    if ans:
        break

print("Yes" if ans else "No")