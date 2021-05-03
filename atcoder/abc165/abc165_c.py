import collections

split_int_input = lambda: [int(v) for v in input().split()]

N, M, Q = split_int_input()
QS = []
for _ in range(Q):
    QS.append(split_int_input())


def get_score(a):
    score = 0
    for q in QS:
        if a[q[1] - 1] - a[q[0] - 1] == q[2]:
            score += q[3]
    return score


ans = 0
tmpdq = collections.deque()
for i in range(1, M + 1):
    tmpdq.append([i])
while len(tmpdq) > 0:
    a = tmpdq.popleft()
    if len(a) == N:
        score = get_score(a)
        ans = max(ans, score)
    else:
        for i in range(a[-1], M + 1):
            tmpdq.append(a + [i])

print(ans)