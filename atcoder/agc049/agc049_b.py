from collections import deque

N = int(input())
S = [int(v) for v in input()]
T = [int(v) for v in input()]

s1dq = deque()
for i in range(N):
    if S[i] == 1:
        s1dq.append(i)

i = 0
cnt = 0
while len(s1dq) > 0:
    if S[i] == T[i]:
        if S[i] == 1:
            s1dq.popleft()
    else:
        if S[i] == 0:
            a = s1dq.popleft()
            S[i], S[a] = 1, 0
        else:
            if len(s1dq) < 2:
                break
            s1dq.popleft()
            a = s1dq.popleft()
            S[i] = S[a] = 0
        cnt += a - i
    i += 1

for i in range(N):
    if S[i] != T[i]:
        cnt = -1
        break

print(cnt)