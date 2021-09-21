import statistics

N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = [int(v) for v in input().split()]
    X.append(x)
    Y.append(y)
x = statistics.median(X)
y = statistics.median(Y)
ans = 0
for i in range(N):
    ans += abs(X[i] - x) + abs(Y[i] - y)
print(int(ans))
