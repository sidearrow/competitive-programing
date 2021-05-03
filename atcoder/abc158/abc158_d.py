from collections import deque

S = deque(input())
Q = int(input())
is_reverse = False
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        is_reverse = not is_reverse
    else:
        if (not is_reverse and q[1] == "1") or (is_reverse and q[1] == "2"):
            S.appendleft(q[2])
        else:
            S.append(q[2])

if is_reverse:
    S.reverse()
print("".join(S))