for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pair = list(map(int, input().split()))

    pair_lst = [0] * (N+1)
    check = [0] * (N+1)

    for i in range(M):
        pair_lst[pair[i * 2]] = pair[i * 2 + 1]
        check[pair[i * 2 + 1]] = 1

    cnt = 0
    for c in range(pair_lst):
        if c == 0:
            cnt +=1
    for x in range
