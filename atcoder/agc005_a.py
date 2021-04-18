from collections import deque

X = input()
a = deque()

for x in X:
    if x == "T" and len(a) > 0 and a[-1] == "S":
        a.pop()
    else:
        a.append(x)

ans = len(a)
print(ans)