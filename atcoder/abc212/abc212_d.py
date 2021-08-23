import heapq

split_int_input = lambda: [int(v) for v in input().split()]

Q = int(input())
xsum = 0
hq = []

for _ in range(Q):
    q = input()
    if q == "3":
        a = heapq.heappop(hq)
        print(a + xsum)
        continue
    p, x = [int(v) for v in q.split()]
    if p == 2:
        xsum += x
    else:
        heapq.heappush(hq, x - xsum)