from test.timer import Timer


def pattern1(num_list):
    res = 0
    for n in num_list:
        res *= 10
        res += n
    return res


def pattern2(num_list):
    res = ""
    for n in num_list:
        res += str(n)
    return int(res)


t = Timer()
t.start()
for _ in range(10 ** 5):
    a = pattern1(list(range(1, 10)))
t.stop()

t.start()
for _ in range(10 ** 5):
    a = pattern2(list(range(1, 10)))
t.stop()