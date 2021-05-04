from collections import deque

s = input()
s = deque(s)

ans = 0
while 1:
    ls = len(s)
    if ls == 0:
        break
    if s[0] == s[-1]:
        s.popleft()
        if ls > 1:
            s.pop()
    else:
        if s[0] == "x":
            ans += 1
            s.popleft()
        elif s[-1] == "x":
            ans += 1
            s.pop()
        else:
            ans = -1
            break

print(ans)