from collections import deque

N = int(input())

ans = 0
dq = deque([3, 5, 7])
while 1:
    a = dq.popleft()
    if a > N:
        break
    if len(set(str(a))) == 3:
        ans += 1
    for v in [3, 5, 7]:
        dq.append(a * 10 + v)

print(ans)