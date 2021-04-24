from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N, Q = split_int_input()
PS = []
for _ in range(N):
    n, t = input().split()
    PS.append((n, int(t)))

dq = deque(PS)
t_sum = 0
while len(dq) > 0:
    n, t = dq.popleft()
    if t <= Q:
        t_sum += t
        print(n, t_sum)
    else:
        t_sum += Q
        dq.append((n, t - Q))
