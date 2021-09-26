N = int(input())

sum_a = 0
diff = []
for _ in range(N):
    a, b = [int(v) for v in input().split()]
    sum_a += a
    diff.append(2 * a + b)
diff.sort()
diff.reverse()

ans = 0
for v in diff:
    if sum_a < 0:
        break
    sum_a -= v
    ans += 1

print(ans)
