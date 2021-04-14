for tc in range(1, int(input())+1):
    n = int(input())

    arr = []
    for row in range(n):
            arr.append([0]*n)

    cnt = 0
    i = 0
    j = 0
    k = 0
    while cnt < n**2:

        for j in range(0+k, n-k):
            cnt += 1
            arr[i][j] = cnt

        for i in range(1+k, n-k):
            cnt += 1
            arr[i][j] = cnt

        for j in range(n-2-k, -1+k, -1):
            cnt += 1
            arr[i][j] = cnt

        for i in range(n-2-k, 0+k, -1):
            cnt += 1
            arr[i][j] = cnt
        k += 1

    print('#{}'.format(tc))
    for ans in arr:
        print(*ans)