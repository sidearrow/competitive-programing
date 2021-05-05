from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

H, W = split_int_input()
h, w = H + 2, W + 2
seen = [False] * (h * w)
dq = deque()
for i in range(h * w):
    if i < w or i % w == 0 or i % w == (w - 1) or i >= (h * w) - w:
        seen[i] = True
for i in range(H):
    for j, v in enumerate(input()):
        if v == "#":
            idx = w * (i + 1) + j + 1
            seen[idx] = True
            dq.append([idx, 0])

ans = 0
while len(dq) > 0:
    a, b = dq.popleft()
    ans = max(ans, b)
    for i in [a - w, a - 1, a + 1, a + w]:
        if not seen[i]:
            dq.append([i, b + 1])
            seen[i] = True

print(ans)