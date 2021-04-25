class SegmentTree:
    def __init__(self, size, init, func, default):
        self.size = size
        self.default = default
        self.tree = [default] * (size * 2)
        self.func = func

        for i, v in enumerate(init, size):
            self.tree[i] = v
        for i in range(size - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def set(self, i, v):
        i += self.size
        self.tree[i] += v
        while i > 1:
            i //= 2
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def get(self, l, r):
        l += self.size
        r += self.size
        vl = self.default
        vr = self.default
        while l < r:
            if l % 2 == 1:
                vl = self.func(vl, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                vr = self.func(self.tree[r], vr)
            l //= 2
            r //= 2
        return self.func(vl, vr)


split_int_input = lambda: [int(v) for v in input().split()]
N, Q = split_int_input()

func = lambda x, y: x + y
st = SegmentTree(N, [0] * N, func, 0)

for _ in range(Q):
    com, x, y = split_int_input()
    if com == 0:
        st.set(x - 1, y)
    else:
        print(st.get(x - 1, y))
