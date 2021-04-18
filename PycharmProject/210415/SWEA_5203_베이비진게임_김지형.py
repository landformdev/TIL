def baby(T):
    for i in range(0, 12, 2):

        if T[i] in A:
            A[T[i]] += 1
        else:
            A[T[i]] = 1

        if T[i] in A and A[T[i]] == 3:
            return 1

        if T[i] + 1 in A and T[i] - 1 in A:
            return 1
        if T[i] - 2 in A and T[i] - 1 in A:
            return 1
        if T[i] + 1 in A and T[i] + 2 in A:
            return 1

        if T[i+1] in B:
            B[T[i+1]] += 1
        else:
            B[T[i+1]] = 1

        if T[i+1] in B and B[T[i+1]] == 3:
            return 2

        if T[i + 1] + 1 in B and T[i + 1] - 1 in B:
            return 2
        if T[i + 1] - 2 in B and T[i + 1] - 1 in B:
            return 2
        if T[i + 1] + 1 in B and T[i + 1] + 2 in B:
            return 2


for tc in range(1, int(input()) + 1):
    A = {}
    B = {}

    turns = list(map(int, input().split()))

    result = baby(turns)

    print('#{}'.format(tc), end=' ')
    if result is None:
        print('0')
    else:
        print(result)
