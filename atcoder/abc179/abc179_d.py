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


split_int_input = lambda: [int(v) for v in input().split()]

N, K = split_int_input()
A = [split_int_input() for _ in range(K)]

st = SegmentTree(N + 1, lambda a, b: a + b, 0)
st.set(1, 1)
mod = 998244353
for i in range(2, N + 1):
    tmp = 0
    for l, r in A:
        _l = i - r
        _r = i - l
        if _r >= 1:
            tmp += st.get(max(1, _l), _r + 1)
            tmp %= mod
    st.set(i, tmp)

print(st.tree[-1])