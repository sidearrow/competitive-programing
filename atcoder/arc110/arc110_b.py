from collections import deque

N = int(input())
T = [int(c) for c in input()]

dq = deque(T)


if N == 1 and dq[0] == 1:
    print(10 ** 10 * 2)
    exit()
if N == 2 and dq[0] == 1 and dq[1] == 1:
    print(10 ** 10)
    exit()


def count_start():
    if dq[0] == 0:
        dq.popleft()
        return 1
    if len(dq) >= 2 and dq[0] == 1 and dq[1] == 0:
        dq.popleft()
        dq.popleft()
        return 1
    if len(dq) >= 3 and dq[0] == 1 and dq[1] == 1 and dq[2] == 0:
        dq.popleft()
        dq.popleft()
        dq.popleft()
        return 1
    return -1


def count_mid():
    cnt = 0
    while len(dq) >= 3:
        a = dq.popleft()
        b = dq.popleft()
        c = dq.popleft()
        if a == 1 and b == 1 and c == 0:
            cnt += 1
            continue
        return -1
    return cnt


def count_end():
    if len(dq) == 0:
        return 0
    if len(dq) == 1:
        if dq[0] == 1:
            return 1
    if len(dq) == 2:
        if dq[0] == 1 and dq[1] == 1:
            return 1
    return -1


cnt = 0
cnt_start = count_start()
if cnt_start == -1:
    print(0)
    exit()
cnt += cnt_start

cnt_mid = count_mid()
if cnt_mid == -1:
    print(0)
    exit()
cnt += cnt_mid

cntend = count_end()
if cntend == -1:
    print(0)
    exit()
cnt += cntend

ans = 10 ** 10 - cnt + 1
print(ans)