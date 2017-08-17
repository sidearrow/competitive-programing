def getResult(data):
    tmp = []
    tmp.append(data)
    n = 2
    total = data
    while n <= 10:
        num = 0
        if (n % 2 == 0):
            num = tmp[n - 2] * 2
        else:
            num = tmp[n - 2] / 3
        tmp.append(num)
        total += num
        n += 1
    return total

while True:
    try:
        tmp = float(input())
        print(getResult(tmp))

    except EOFError:
        break
