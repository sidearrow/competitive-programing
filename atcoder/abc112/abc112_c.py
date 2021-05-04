split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
Z = [split_int_input() for _ in range(N)]
Z = sorted(Z, key=lambda v: v[2], reverse=True)

ans = None
for cx in range(101):
    for cy in range(101):
        x, y, h = Z[0]
        ch = h + abs(x - cx) + abs(y - cy)
        is_valid = True
        for _x, _y, _h in Z[1:]:
            if _h != max(ch - abs(cx - _x) - abs(cy - _y), 0):
                is_valid = False
                break
        if is_valid:
            ans = [cx, cy, ch]

print(*ans)