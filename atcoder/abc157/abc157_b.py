A = []

for i in range(3):
    A.append(input().split())

N = int(input())

for n in range(N):
    b = input()
    for i, row in enumerate(A):
        for j, col in enumerate(row):
            if b == col:
                A[i][j] = True

res = False
for i in range(3):
    if A[i][0] == True and A[i][1] == True and A[i][2] == True:
        res = True
    if A[0][i] == True and A[1][i] == True and A[2][i] == True:
        res = True
if A[0][0] == True and A[1][1] == True and A[2][2] == True:
    res = True
if A[2][0] == True and A[1][1] == True and A[0][2] == True:
    res = True

print('Yes') if res else print('No')
