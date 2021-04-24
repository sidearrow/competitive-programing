from collections import deque

N = int(input())

dq = deque()
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "insert":
        dq.appendleft(cmd[1])
        continue
    if cmd[0] == "delete":
        try:
            dq.remove(cmd[1])
        except:
            pass
        continue
    if cmd[0] == "deleteFirst":
        dq.popleft()
        continue
    if cmd[0] == "deleteLast":
        dq.pop()
        continue

print(*dq)