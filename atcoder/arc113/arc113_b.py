A, B, C = [int(v) for v in input().split()]

a = A % 10
loop = [a]
tmp = a
while True:
    tmp = (tmp * a) % 10
    if tmp == loop[0]:
        break
    loop.append(tmp)

mod = pow(B, C, len(loop))
print(loop[mod - 1])
