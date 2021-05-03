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