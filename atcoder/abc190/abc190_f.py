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


split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
A = split_int_input()

ans = 0
bit = BIT(N)
for i, a in enumerate(A):
    ans += i - bit.sum(a + 1)
    bit.add(a + 1, 1)
print(ans)
for i in range(N - 1):
    a = A[i]
    ans = ans - a + (N - bit.sum(a + 1))
    print(ans)
