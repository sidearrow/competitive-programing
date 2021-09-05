class BIT:
    def __init__(self, n: int):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def bisect_left(self, w):
        res = 0
        tmp_sum = 0
        for i in range(self.depth, -1, -1):
            k = res + (1 << i)
            if k <= self.size and tmp_sum + self.tree[k] < w:
                tmp_sum += self.tree[k]
                res = k
        return res + 1


split_int_input = lambda: [int(v) for v in input().split()]

L, Q = split_int_input()
C = []
X = []
for _ in range(Q):
    c, x = split_int_input()
    C.append(c)
    X.append(x)

X.append(0)
X.append(L)
sorted_set_x = sorted(set(X))
compressed_x = {k: i for i, k in enumerate(sorted_set_x)}

bit = BIT(len(compressed_x))
bit.add(bit.size, 1)
for i in range(Q):
    x_idx = compressed_x[X[i]] + 1
    if C[i] == 1:
        bit.add(x_idx, 1)
    else:
        x_idx_sum = bit.sum(x_idx)
        l = bit.bisect_left(x_idx_sum)
        r = bit.bisect_left(x_idx_sum + 1)
        print(sorted_set_x[r - 1] - sorted_set_x[l - 1])