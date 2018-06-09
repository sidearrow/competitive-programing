def decisionPN(data):
    i = 2
    while i <= data / 2:
        if data % i == 0:
            return False
        i += 1
    return True

def getResult(data):
    result = 0
    i = 2
    while i <= data / 2:
        if decisionPN(i) and decisionPN(data - i):
            print(i)
            result += 1
        i += 1
    return result

while True:
    tmp = int(input())
    if tmp == 0:
        break
    print(getResult(tmp))
