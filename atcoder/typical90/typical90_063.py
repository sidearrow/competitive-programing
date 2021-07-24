from collections import Counter


split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
P = [split_int_input() for _ in range(H)]

ans = 0
for bit in range(2 ** H):
    memo = []
    hidxs = []
    for i in range(H):
        if bit >> i & 1:
            hidxs.append(i)
    for w in range(W):
        tmp = -1
        for h in hidxs:
            if tmp == -1:
                tmp = P[h][w]
            else:
                if tmp != P[h][w]:
                    tmp = -1
                    break
        if tmp != -1:
            memo.append(tmp)
    if len(memo) > 0:
        mc = Counter(memo).most_common(1)[0][1]
        ans = max(ans, mc * len(hidxs))

print(ans)