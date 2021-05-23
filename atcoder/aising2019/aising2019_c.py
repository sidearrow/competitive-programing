from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
S = [list(input()) for _ in range(H)]

seen = [[False] * W for _ in range(H)]
ans = 0
for h in range(H):
    for w in range(W):
        if seen[h][w]:
            continue
        dq = deque()
        dq.append([h, w])
        memo = {"#": 0, ".": 0}
        memo[S[h][w]] += 1
        seen[h][w] = True
        while len(dq) > 0:
            h1, w1 = dq.popleft()
            nxt = [[h1 - 1, w1], [h1 + 1, w1], [h1, w1 - 1], [h1, w1 + 1]]
            for h2, w2 in nxt:
                if (
                    0 <= h2 < H
                    and 0 <= w2 < W
                    and not seen[h2][w2]
                    and S[h1][w1] != S[h2][w2]
                ):
                    dq.appendleft([h2, w2])
                    memo[S[h2][w2]] += 1
                    seen[h2][w2] = True
        ans += memo["#"] * memo["."]

print(ans)