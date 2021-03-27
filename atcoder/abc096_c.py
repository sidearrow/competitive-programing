split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
s = []
for _ in range(H):
    row = [v == "#" for v in input()]
    s.append(row)

ans = True
for i in range(H):
    for j in range(W):
        if not s[i][j]:
            continue
        if i > 0 and s[i - 1][j]:
            continue
        if i < H - 1 and s[i + 1][j]:
            continue
        if j > 0 and s[i][j - 1]:
            continue
        if j < W - 1 and s[i][j + 1]:
            continue
        ans = False
        break
    if not ans:
        break

print("Yes" if ans else "No")
