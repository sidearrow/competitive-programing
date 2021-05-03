import sys

input = sys.stdin.readline

M, H = [int(v) for v in input().split()]

if H % M == 0:
    print("Yes")
else:
    print("No")