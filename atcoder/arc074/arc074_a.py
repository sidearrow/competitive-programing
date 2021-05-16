split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()

ans = H * W


for i in range(1, (H + 1) // 2 + 1):
    a = i * W
    h = H - i
    b = h // 2 * W
    c = (H - h // 2 - i) * W
    ans = min(ans, max(a, b, c) - min(a, b, c))
    b = W // 2 * h
    c = (W - W // 2) * h
    ans = min(ans, max(a, b, c) - min(a, b, c))

for i in range(1, (W + 1) // 2 + 1):
    a = i * H
    w = W - i
    b = w // 2 * H
    c = (W - w // 2 - i) * H
    ans = min(ans, max(a, b, c) - min(a, b, c))
    b = H // 2 * w
    c = (H - H // 2) * w
    ans = min(ans, max(a, b, c) - min(a, b, c))

print(ans)