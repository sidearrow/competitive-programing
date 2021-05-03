N = input()
x = list(map(int, input().split()))

res_m = 0
res_u = 0
res_c = 0
for v in x:
    absv = abs(v)
    res_m += absv
    res_u += absv ** 2
    res_c = max(res_c, absv)
res_u **= 0.5

print(res_m)
print(res_u)
print(res_c)
