import sys

input = sys.stdin.readline

N = int(input())

res = 0
for i in range(1, N):
    res += N / (N - i)

print(res)