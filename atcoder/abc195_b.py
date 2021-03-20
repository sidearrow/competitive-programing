import sys
import math

input = sys.stdin.readline

A, B, H = [int(v) for v in input().split()]

h = H * 1000
mx = math.floor(h / A)
mn = math.ceil(h / B)

if mx < mn:
    print("UNSATISFIABLE")
else:
    print(str(mn) + " " + str(mx))