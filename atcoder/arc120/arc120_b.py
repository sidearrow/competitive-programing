split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
S = [list(input()) for _ in range(H)]

memo = [set() for _ in range(H + W)]
valid = True
for h in range(H):
    for w in range(W):
        memo[h + w].add(S[h][w])

ans = 1
for v in memo:
    if "R" in v and "B" in v:
        print(0)
        exit()
    if v == set(["."]):
        ans = ans * 2 % 998244353

print(ans)