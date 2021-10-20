import sys

_rl = sys.stdin.readline
_rl2 = lambda: [int(v) for v in _rl().split()]

A, B = _rl2()
x = (A + B) // 2
y = (A - B) // 2
print(x, y)
