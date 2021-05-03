split_int_input = lambda: [int(v) for v in input().split()]
sx, sy, tx, ty = split_int_input()
w = tx - sx
h = ty - sy

ans = "U" * h + "R" * w
ans += "D" * h + "L" * w
ans += "L" + "U" * (h + 1) + "R" * (w + 1) + "D"
ans += "R" + "D" * (h + 1) + "L" * (w + 1) + "U"

print(ans)