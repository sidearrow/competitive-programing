from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()
B = split_int_input()

ans = 0
for i in range(N):
    if A[i] == B[i]:
        continue
    swap = False
    for j in range(N):
        if A[j] is None:
            continue
        diff = j - i
        if A[j] + diff == B[i]:
            A[j] = A[i] - diff
            A[i] = None
            ans += diff
            swap = True
        else:
            A[j] -= 1
    if not swap:
        print(-1)
        exit()