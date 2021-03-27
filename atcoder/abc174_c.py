K = int(input())

ans = 1
tmp = 7
modset = set()
while 1:
    if tmp >= K:
        tmp = tmp % K
        if tmp == 0:
            break
        if tmp in modset:
            ans = -1
            break
        else:
            modset.add(tmp)
    ans += 1
    tmp = tmp * 10 + 7

print(ans)