import sys

readline = sys.stdin.readline
readline2 = lambda: [int(v) for v in readline().split()]

compressed = lambda v: {k: i for i, k in enumerate(sorted(set(v)))}

LRUD = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D": [1, 0]}

lower_az = [chr(i) for i in range(97, 123)]
upper_az = [chr(i) for i in range(65, 91)]

sys.setrecursionlimit(10 ** 7)