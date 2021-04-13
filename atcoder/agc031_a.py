from collections import Counter

N = int(input())
S = input()

sc = Counter(S)
ans = 1
mod = 10 ** 9 + 7
for num in sc.values():
    ans *= num + 1
    ans %= mod
ans -= 1
ans %= mod
print(ans)