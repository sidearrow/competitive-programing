results = []

def decisionPN (n):
    flag = 0
    i = 2
    while i <= int(n / 2):
        if (n % i == 0):
            flag = 1
            break
        i += 1
    if (flag == 0):
        return True
    else:
        return False

def getResult(n):
    i = 2
    num = 0
    result = 0
    while num < n:
        flag = decisionPN(i)
        if (flag):
            num += 1
            result += i
        i += 1
    return result

while True:
    tmp = int(input())
    if tmp == 0:
        break
    results.append(getResult(tmp))

print(results)

for result in results:
    print(result)
