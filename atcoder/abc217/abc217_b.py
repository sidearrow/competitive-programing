a = set(["ABC", "ARC", "AGC", "AHC"])
for _ in range(3):
    s = input()
    a.remove(s)

print(a.pop())
