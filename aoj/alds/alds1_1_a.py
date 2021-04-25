split_int_input = lambda: [int(v) for v in input().split()]


def insertion_sort(a, n):
    for i in range(1, n):
        print(*a)
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v
    print(*a)


N = int(input())
A = split_int_input()

insertion_sort(A, N)