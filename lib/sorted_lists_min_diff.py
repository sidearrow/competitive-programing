import typing


def sorted_lists_min_diff(la: typing.List[int], lb: typing.List[int]):
    res = float("inf")
    bidx = 0
    for a in la:
        while bidx + 1 < len(lb) and lb[bidx + 1] <= a:
            bidx += 1
        res = min(res, abs(a - lb[bidx]))
        if bidx + 1 < len(lb):
            res = min(res, abs(a - lb[bidx + 1]))
    return res


a = [1, 4, 6]
b = [3, 8]
assert sorted_lists_min_diff(a, b) == 1

a = [10, 12]
b = [3, 5, 7]
assert sorted_lists_min_diff(a, b) == 3