from collections import Counter

split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = [split_int_input() for _ in range(N)]

if N == 1:
    print(1)
    exit()

s = []
for i in range(N):
    for j in range(i + 1, N):
        s.append((A[i][0] - A[j][0], A[i][1] - A[j][1]))
        s.append((A[j][0] - A[i][0], A[j][1] - A[i][1]))

s = Counter(s)
print(N - s.most_common()[0][1])