N = int(input())

ans = []
n = N
for i in [2] + list(range(3, int(N ** 0.5) + 1, 2)):
    while n % i == 0:
        n //= i
        ans.append(i)
if n != 1:
    ans.append(n)

print("{}:".format(N), *ans)
