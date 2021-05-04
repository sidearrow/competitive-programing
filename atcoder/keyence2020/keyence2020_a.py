from math import ceil

H = int(input())
W = int(input())
N = int(input())

ans = ceil(N / max(H, W))
print(ans)