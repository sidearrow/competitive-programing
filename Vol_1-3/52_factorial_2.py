results = []

def fact(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result

def get_result(n):
    tmp = list(reversed(list(str(n))))
    for i in range(len(tmp)):
        if (tmp[i] != '0'):
            return i

while True:
    tmp = int(input())
    if tmp == 0:
        break
    results.append(get_result(fact(tmp)))

for result in results:
    print(result)
