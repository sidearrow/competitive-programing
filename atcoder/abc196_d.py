split_int_input = lambda: [int(v) for v in input().split()]

H, W, A, B = split_int_input()
ans = 0


class DFS:
    def __init__(self) -> None:
        self.ans = 0

    def dfs(self, i, bit, a, b):
        if i == H * W:
            if a == 0 and b == 0:
                self.ans += 1
            return
        if bit >> i & 1:
            self.dfs(i + 1, bit, a, b)
        if b > 0:
            next_bit = bit | 1 << i
            self.dfs(i + 1, next_bit, a, b - 1)
        if a > 0:
            if i % W != W - 1 and not bit >> i + 1 & 1:
                next_bit = bit | 1 << i | 1 << i + 1
                self.dfs(i + 1, next_bit, a - 1, b)
            if i + W < H * W:
                next_bit = bit | 1 << i | 1 << i + W
                self.dfs(i + 1, next_bit, a - 1, b)


dfs = DFS()
dfs.dfs(0, 0, A, B)
print(dfs.ans)
