split_int_input = lambda: [int(v) for v in input().split()]

T = int(input())
for _ in range(T):
    N = int(input())
    A = split_int_input()
    AL = len(A)
    ans = []
    for i in range(N ** 2):
        is_break = True
        ng = False
        i = i % 2
        for j in range(AL - 1):
            if A[j] > A[j + 1]:
                if i != j % 2:
                    ng = True
                else:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    ans.append(j + 1)
                    is_break = False
                    ng = False
                    break
        if ng:
            idx = AL - 2
            if idx % 2 != i:
                idx -= 1
            ans.append(idx + 1)
            A[idx], A[idx + 1] = A[idx + 1], A[idx]
            continue
        if is_break:
            break
    print(len(ans))
    print(*ans)
