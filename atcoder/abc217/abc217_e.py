import heapq
from collections import deque

Q = int(input())

adq = deque()
ahq = []

for _ in range(Q):
    q = input()
    if q == "2":
        if len(ahq) > 0:
            print(heapq.heappop(ahq))
        else:
            print(adq.popleft())
        continue
    if q == "3":
        while len(adq) > 0:
            heapq.heappush(ahq, adq.pop())
        continue
    x = int(q.split()[1])
    adq.append(x)
