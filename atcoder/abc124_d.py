split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
S = input()


new_s = [[int(S[0]), 1]]
for s in S[1:]:
    s = int(s)
    if s == new_s[-1][0]:
        new_s[-1][1] += 1
    else:
        new_s.append([s, 1])

ans = 0
r = 0
k = 0
tmp_ans = 0
len_new_s = len(new_s)
for l in range(len_new_s):
    while r < len_new_s:
        if k == K and new_s[r][0] == 0:
            break
        if new_s[r][0] == 0:
            k += 1
        tmp_ans += new_s[r][1]
        r += 1
    ans = max(ans, tmp_ans)
    if new_s[l][0] == 0:
        k -= 1
    tmp_ans -= new_s[l][1]

print(ans)