import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N = int(readline())
A = readline2()
B = readline2()
B.sort()


def check(x):
    tmp = [a ^ x for a in A]
    tmp.sort()
    for i in range(N):
        if tmp[i] != B[i]:
            return False
    return True


ans = set()
for b in B:
    x = A[0] ^ b
    if check(x):
        ans.add(x)
ans = sorted(ans)
print(len(ans))
for v in ans:
    print(v)
