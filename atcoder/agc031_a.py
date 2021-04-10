N = int(input())
S = input()

tmp = {S[0]: 1}
ans = 1
mod = 10 ** 9 + 7
for s in S[1:]:
    print(ans, s, tmp)
    _ans = 1
    _a = tmp.get(s, 0)
    b = (ans - _a) * 2 % mod
    _ans += _a + b
    _ans %= mod
    _tmp = {}
    for k, v in tmp.items():
        _tmp[k] = v * 2
    _tmp[s] = ans + 1
    ans = _ans
    tmp = _tmp

print(ans)