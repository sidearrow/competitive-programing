S = input()
K = int(input())

az_lst = [chr(i) for i in range(97, 123)]
dists = {v: 26 - i for i, v in enumerate(az_lst)}
dists["a"] = 0

ans = []
for s in S:
    if dists[s] <= K:
        K -= dists[s]
        ans.append("a")
    else:
        ans.append(s)

ans[-1] = az_lst[az_lst.index(ans[-1]) + K % 26]
ans = "".join(ans)
print(ans)