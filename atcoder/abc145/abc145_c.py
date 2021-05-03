from itertools import permutations


def calc_distance(xy1: list, xy2: list):
    return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5


def calc_all_distance(xy_list: list):
    res = 0
    for i, xy in enumerate(xy_list):
        if i == 0:
            continue
        res += calc_distance(xy_list[i - 1], xy)
    return res


def main():
    n = int(input())
    xy = [list(map(int, input().split())) for i in range(n)]
    perm = permutations(list(range(n)), n)
    res = []
    for v in perm:
        xy_list = [xy[i] for i in v]
        res.append(calc_all_distance(xy_list))
    print(sum(res) / len(res))


main()