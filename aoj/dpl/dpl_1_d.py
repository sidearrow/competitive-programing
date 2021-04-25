import bisect

N = int(input())
A = [int(input()) for _ in range(N)]

lis = [A[0]]
for a in A[1:]:
    if a > lis[-1]:
        lis.append(a)
    else:
        lis[bisect.bisect_left(lis, a)] = a

print(len(lis))