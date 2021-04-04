from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]
H, W = split_int_input()
N = int(input())
a = split_int_input()

b = deque()
for i, v in enumerate(a):
    for _ in range(v):
        b.append(i + 1)

ans = []
tmp = deque()
for _ in range(H * W):
    tmp.append(b.popleft())
    if len(tmp) == W:
        ans.append(tmp)
        tmp = deque()

for i, v in enumerate(ans):
    if i % 2 == 0:
        print(*v)
    else:
        print(*reversed(v))