N = int(input())
A = list(map(int, input().split()))
res = 0
while True:
    isBreak = False
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] /= 2
        else:
            isBreak = True
            break
    if isBreak:
        break
    res += 1
print(res)
