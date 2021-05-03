split_int_input = lambda: [int(v) for v in input().split()]


class LazySegmentTree:
    def __init__(self, size, default, func):
        self.size = size
        self.default = default
        self.tree = [default] * (size * 2)
        self.func = func
        self.lazy = [None] * (size * 2)

    def __get_indexes(self, l, r):
        l += self.size
        r += self.size
        _l = (l // (l & -l)) >> 1
        _r = (r // (r & -r)) >> 1
        res = []
        while l < r:
            if r <= _r:
                res.append(r)
            if l <= _l:
                res.append(l)
            l >>= 1
            r >>= 1
        while l:
            res.append(l)
            l >>= 1
        return res

    def __propagate(self, indexes):
        for i in reversed(indexes):
            v = self.lazy[i]
            if v is not None:
                self.lazy[2 * i] = self.tree[2 * i] = v
                self.lazy[2 * i + 1] = self.tree[2 * i + 1] = v
                self.lazy[i] = None

    def update(self, l, r, a):
        indexes = self.__get_indexes(l, r)
        self.__propagate(indexes)
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                self.lazy[l] = self.tree[l] = a
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] = self.tree[r] = a
            l >>= 1
            r >>= 1
        for i in indexes:
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def get(self, l, r):
        self.__propagate(self.__get_indexes(l, r))
        l += self.size
        r += self.size
        res = self.default
        while l < r:
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.func(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res


W, N = split_int_input()

zahyo_set = set()
A = []
for _ in range(N):
    l, r = split_int_input()
    A.append([l, r])
    zahyo_set.add(l)
    zahyo_set.add(r)
compressed_zahyo_dict = {}
for i, v in enumerate(sorted(zahyo_set)):
    compressed_zahyo_dict[v] = i
for i in range(N):
    A[i][0] = compressed_zahyo_dict[A[i][0]]
    A[i][1] = compressed_zahyo_dict[A[i][1]]

st = LazySegmentTree(len(compressed_zahyo_dict), 0, max)
for l, r in A:
    h = st.get(l, r + 1) + 1
    print(h)
    st.update(l, r + 1, h)