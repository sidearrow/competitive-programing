import sys

readline = sys.stdin.readline
readline_split_int = lambda: [int(v) for v in readline().split()]

compressed = lambda v: {k: i for i, k in enumerate(sorted(set(v)))}

MODINT = 10 ** 9 + 7

lower_az = [chr(i) for i in range(97, 123)]
upper_az = [chr(i) for i in range(65, 91)]

sys.setrecursionlimit(10 ** 7)