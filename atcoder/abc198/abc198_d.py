import itertools


def str_to_num(s, n):
    res = 0
    for _s in s:
        res *= 10
        res += n[_s]
    return res


a = input()
b = input()
c = input()
strs = list(set(a + b + c))
str_kind_num = len(strs)
if str_kind_num > 10:
    print("UNSOLVABLE")
    exit()
nums = itertools.permutations(range(10), str_kind_num)
a0 = a[0]
b0 = b[0]
c0 = c[0]
for ns in nums:
    m = {strs[i]: ns[i] for i in range(str_kind_num)}
    if m[a0] == 0 or m[b0] == 0 or m[c0] == 0:
        continue
    abc = []
    for s in [a, b, c]:
        tmp = 0
        for _c in s:
            tmp *= 10
            tmp += m[_c]
        abc.append(tmp)
    if abc[0] + abc[1] == abc[2]:
        print(abc[0])
        print(abc[1])
        print(abc[2])
        exit()
print("UNSOLVABLE")