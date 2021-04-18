split_int_input = lambda: [int(v) for v in input().split()]

N = int(input())
a = []
b = []
for _ in range(N):
    x, y = split_int_input()
    a.append(x + y)
    b.append(x - y)

a = sorted(a, reverse=True)
b = sorted(b, reverse=True)

ans = max(a[0] - a[-1], b[0] - b[-1])
print(ans)
