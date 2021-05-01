N = int(input())

users = set()
for i in range(1, N + 1):
    s = input()
    if s not in users:
        print(i)
        users.add(s)