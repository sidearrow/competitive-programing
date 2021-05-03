T = int(input())
for _ in range(T):
    n = int(input())
    if n % 2 == 1:
        print("Odd")
    elif (n // 2) % 2 == 0:
        print("Even")
    else:
        print("Same")
