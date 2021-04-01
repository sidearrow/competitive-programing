from collections import deque
from timer import Timer
from random import randint

t = Timer()


def pop_list_vs_deque():
    n = 10 ** 5
    a = [0] * n
    t.start()
    for _ in range(n):
        b = a.pop(0)
    t.stop()
    t.reset()

    a = [0] * n
    t.start()
    a = deque(a)
    for _ in range(n):
        b = a.popleft()
    t.stop()


def sort_list_vs_deque():
    n = 10 ** 6
    a = [randint(0, n) for _ in range(n)]

    # list
    t.start()
    a.sort()
    t.stop()

    # list sorted
    t.start()
    a = sorted(a)
    t.stop()

    a = deque(a)
    # deque
    t.start()
    a = sorted(a)
    t.stop()


sort_list_vs_deque()