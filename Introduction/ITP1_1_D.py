tmp = int(input())

h = tmp // 3600
tmp = tmp % 3600

m = tmp // 60
s = tmp % 60

print(str(h) + ':' + str(m) + ':' + str(s))
