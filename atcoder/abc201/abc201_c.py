S = list(input())

ans = 0
for i in range(10 ** 4):
    st = set(str(i).zfill(4))
    valid = True
    for j, s in enumerate(S):
        j = str(j)
        if s == "o" and j not in st:
            valid = False
            break
        if s == "x" and j in st:
            valid = False
            break
    if valid:
        ans += 1

print(ans)