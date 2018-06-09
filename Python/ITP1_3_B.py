data = []    
while True:
    tmp = input()
    if tmp == '0':
        break
    data.append(tmp)

for i in range(len(data)):
    print('Case ' + str(i + 1) + ': ' + data[i - 1])
