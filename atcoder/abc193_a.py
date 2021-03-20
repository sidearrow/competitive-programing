import sys

input = sys.stdin.readline

A, B = map(int, input().split())
res = ((A - B) / A) * 100
print(res)
