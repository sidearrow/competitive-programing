import sys
import itertools

input = sys.stdin.readline

N = int(input())
A = [int(v) for v in input().split()]

tmp = [0 for _ in range(401)]
c = [idx for idx in range(401)]

for v in A:
    tmp[v + 200] += 1

res = 0
for v in itertools.combinations(c, 2):
    res += (v[0] - v[1]) ** 2 * tmp[v[0]] * tmp[v[1]]

print(res)
