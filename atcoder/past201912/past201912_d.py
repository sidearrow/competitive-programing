import sys

readline = sys.stdin.readline

N = int(readline())
memo = [0] * N
for _ in range(N):
    a = int(readline())
    memo[a - 1] += 1

x = y = None
for i, n in enumerate(memo, 1):
    if n == 0:
        x = i
    elif n == 2:
        y = i

if x is None and y is None:
    print("Correct")
else:
    print(y, x)
