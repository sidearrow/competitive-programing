from collections import deque

K = int(input())

dq = deque(range(1, 10))
cnt = 0
n = -1
while 1:
    n = dq.popleft()
    cnt += 1
    if cnt == K:
        break
    mod = n % 10
    for i in range(-1, 2):
        next = mod + i
        if 0 <= next <= 9:
            dq.append(n * 10 + next)
print(n)