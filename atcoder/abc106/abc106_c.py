s = input()
k = int(input())

for _s in s:
    if _s == "1":
        k -= 1
        if k == 0:
            print(_s)
            break
        else:
            continue
    else:
        print(_s)
        break