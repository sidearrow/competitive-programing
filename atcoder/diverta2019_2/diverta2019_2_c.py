from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()

p = deque()
m = deque()
for a in sorted(A):
    if a > 0:
        p.append(a)
    else:
        m.append(a)

if len(p) == 0:
    p.append(m.pop())
if len(m) == 0:
    m.append(p.popleft())

ans = []
while len(p) > 1:
    y = p.popleft()
    ans.append([m[0], y])
    m[0] -= y
while len(m) > 0:
    y = m.popleft()
    ans.append([p[0], y])
    p[0] -= y
print(p[0])
for x, y in ans:
    print(x, y)