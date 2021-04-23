N = int(input())

is_first = False
for _ in range(N):
    a = int(input())
    if a % 2 == 1:
        is_first = True

print("first" if is_first else "second")