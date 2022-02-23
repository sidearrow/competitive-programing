import sys

readline = sys.stdin.readline

A, B = readline().strip().split()
A = list(reversed(A))
B = list(reversed(B))

kuriagari = False
for i in range(100):
    if i >= len(A) or i >= len(B):
        break
    if int(A[i]) + int(B[i]) >= 10:
        kuriagari = True
        break

if kuriagari is True:
    print("Hard")
else:
    print("Easy")
