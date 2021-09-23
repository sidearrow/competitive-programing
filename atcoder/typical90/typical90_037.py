class SegmentTree:
    def __init__(self, size, func, default):
        self.size = size
        self.default = default
        self.tree = [default] * (size * 2)
        self.func = func

    def set(self, i, v):
        i += self.size
        self.tree[i] = v
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


input_split_int = lambda: [int(v) for v in input().split()]

W, N = input_split_int()
st = SegmentTree(W + 1, max, -1)
st.set(0, 0)

for _ in range(N):
    l, r, v = input_split_int()
    for i in range(W, l - 1, -1):
        _l = max(i - r, 0)
        _r = i - l
        _v = st.get(_l, _r + 1)
        if _v != -1:
            _v += v
            if _v > st.tree[i + W + 1]:
                st.set(i, _v)

ans = st.tree[W + W + 1]
print(ans)
