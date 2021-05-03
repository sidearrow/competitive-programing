import sys

input = sys.stdin.readline

N = int(input())

res = 0
for i in range(3, len(str(N)) + 1):
    if i % 3 == 1:
        res += N - (10 ** (i - 1)) + 1

print(res)