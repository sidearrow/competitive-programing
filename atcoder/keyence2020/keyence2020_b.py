from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]
N = int(input())
robots = []
for _ in range(N):
    x, l = split_int_input()
    robots.append([x - l, x + l])
robots = deque(sorted(robots, key=lambda v: v[1]))

ans = 0
x = -(10 ** 10)
while 1:
    l, r = robots.popleft()
    if l >= x:
        ans += 1
        x = r
    if len(robots) == 0:
        break

print(ans)