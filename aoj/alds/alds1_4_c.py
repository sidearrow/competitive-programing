N = int(input())

s = set()
for _ in range(N):
    q = input().split()
    if q[0] == "insert":
        s.add(q[1])
    else:
        print("yes" if q[1] in s else "no")