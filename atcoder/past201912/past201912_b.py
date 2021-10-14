import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

N = int(readline())
prev = int(readline())
for _ in range(N - 1):
    now = int(readline())
    if prev == now:
        print("stay")
    elif prev > now:
        print("down {}".format(prev - now))
    else:
        print("up {}".format(now - prev))
    prev = now
