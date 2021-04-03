from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]
N, C, K = split_int_input()
T = [int(input()) for _ in range(N)]
T = deque(sorted(T))

ans = 0
while 1:
    if len(T) == 0:
        break
    ans += 1
    t = T.popleft()
    t += K
    c = 1
    while 1:
        if c >= C or len(T) == 0 or T[0] > t:
            break
        T.popleft()
        c += 1

print(ans)