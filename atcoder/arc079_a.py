from queue import Queue

split_int_input = lambda: [int(v) for v in input().split()]

N, M = split_int_input()
c = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = split_int_input()
    c[a].append(b)

q = Queue()
q.put([1, 0])
ans = False
while 1:
    if q.empty():
        break
    t, num = q.get()
    if t == N:
        ans = True
        break
    for v in c[t]:
        if num < 2:
            q.put([v, num + 1])

print("POSSIBLE" if ans else "IMPOSSIBLE")