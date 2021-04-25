from collections import deque


S = input().split()

tmp = deque()
for s in S:
    if s == "+":
        b, a = tmp.pop(), tmp.pop()
        tmp.append(a + b)
        continue
    if s == "-":
        b, a = tmp.pop(), tmp.pop()
        tmp.append(a - b)
        continue
    if s == "*":
        b, a = tmp.pop(), tmp.pop()
        tmp.append(a * b)
        continue
    tmp.append(int(s))

print(tmp[0])