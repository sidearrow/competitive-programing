from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]
X, Y, A, B, C = split_int_input()
P = split_int_input()
Q = split_int_input()
R = split_int_input()

p = sorted(P, reverse=True)[:X]
q = sorted(Q, reverse=True)[:Y]
pq = deque(sorted(p + q))
r = deque(sorted(R, reverse=True))

select_r = deque()
while 1:
    if pq[0] < r[0]:
        pq.popleft()
        select_r.append(r.popleft())
        if len(r) == 0:
            break
    else:
        break

ans = sum(pq) + sum(select_r)
print(ans)