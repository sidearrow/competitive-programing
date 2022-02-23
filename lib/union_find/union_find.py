class UnionFind:
    ROOT = -1

    def __init__(self, n: int):
        self.parent = [self.ROOT] * n
        self.size = [1] * n

    def get_root(self, x: int) -> int:
        hist = []
        while self.parent[x] != self.ROOT:
            hist.append(x)
            x = self.parent[x]
        for y in hist:
            self.parent[y] = x
        return x

    def unite(self, x: int, y: int):
        rx, ry = self.get_root(x), self.get_root(y)
        if rx == ry:
            return
        if self.size[ry] > self.size[rx]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
