from collections import deque

N = int(input())
if N == 1:
    print("a")
    exit()

dq = deque(["a"])
ans = []
while len(dq) > 0:
    s = dq.popleft()
    for i in range(97, ord(max(s)) + 2):
        nxt = "".join([s, chr(i)])
        if len(nxt) == N:
            ans.append(nxt)
        else:
            dq.append(nxt)

print("\n".join(ans))