import sys

sys.setrecursionlimit(10 ** 7)


def insert(t, v):
    if t[0] is None:
        t[0] = v
        return
    y = None
    x = t
    while x is not None:
        y = x
        x = x[1] if v < x[0] else x[2]
    if v < y[0]:
        y[1] = [v, None, None]
    else:
        y[2] = [v, None, None]


def inorder_walk(t, res):
    res.append(t[0])
    if t[1] is not None:
        inorder_walk(t[1], res)
    if t[2] is not None:
        inorder_walk(t[2], res)


def preorder_walk(t, res):
    if t[1] is not None:
        preorder_walk(t[1], res)
    res.append(t[0])
    if t[2] is not None:
        preorder_walk(t[2], res)


bst = [None, None, None]
N = int(input())
for _ in range(N):
    q = input().split()
    if q[0] == "insert":
        insert(bst, int(q[1]))
    else:
        res = []
        preorder_walk(bst, res)
        print("", *res)
        res = []
        inorder_walk(bst, res)
        print("", *res)
