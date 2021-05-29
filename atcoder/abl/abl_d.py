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
A = [int(input()) for _ in range(N)]

f = lambda a, b: max(a, b)
st = SegmentTree(300001, f, 0)
for a in A:
    l = max(0, a - K)
    r = min(a + K, 300000) + 1
    tmp = st.get(l, r) + 1
    st.set(a, tmp)

ans = st.get(0, 300001)
print(ans)