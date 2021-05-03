import sys
import math

input = sys.stdin.readline

N = int(input())

mx = int(N ** 0.5 // 1)

s = set()
for i in range(2, mx + 1):
    mx = math.floor(math.log(N, i))
    for j in range(2, mx + 1):
        tmp = i ** j
        s.add(tmp)

print(N - len(s))