N, K = map(int, input().split())

def getNum(num):
    res = 0
    while True:
        if num >= K:
            break
        res += 1
        num *= 2
    return res

res = 0
for i in range(1, N+1):
    res += (1 / N) * (0.5 ** getNum(i))
print(res)
