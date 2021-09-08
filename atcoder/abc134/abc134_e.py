from bisect import bisect_right

N = int(input())
A = [int(input()) for _ in range(N)]
A.reverse()

l = [A[0]]
for a in A[1:]:
    if a >= l[-1]:
        l.append(a)
    else:
        l[bisect_right(l, a)] = a
print(len(l))
