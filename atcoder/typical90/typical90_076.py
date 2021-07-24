from collections import deque

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()

suma = sum(A)
if suma % 10 != 0:
    print("No")
    exit()

b = suma // 10

for i in range(N):
    A.append(A[i])

tmp = 0
dq = deque()
ans = False
for a in A:
    dq.append(a)
    tmp += a
    while tmp > b:
        rm = dq.popleft()
        tmp -= rm
    if tmp == b:
        ans = True

if ans:
    print("Yes")
else:
    print("No")