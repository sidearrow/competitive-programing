data_num = int(input())
results = []

for i in range(data_num):
    data = input()
    min = int(''.join(sorted(list(data))))
    max = int(''.join(sorted(list(data), reverse=True)))
    results.append(max - min)

for result in results:
    print(result)
