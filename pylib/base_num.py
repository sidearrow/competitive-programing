def convert_base_num(target: int, to: int):
    target = str(target)
    l = len(target) - 1
    res = 0
    for i, v in enumerate(target):
        res += (to ** (l - i)) * int(v)
    return res


assert convert_base_num(100, 2) == 4