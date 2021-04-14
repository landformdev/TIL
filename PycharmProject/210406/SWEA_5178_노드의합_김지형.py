for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())  # N은 노드의 갯수

    ans = [0]*(N+1)
    def perfect(n):
        if n*2 <= N:
            perfect(n*2)
            ans[n] += ans[n * 2]
        if n*2+1 <= N:
            perfect(n*2+1)
            ans[n] += ans[n * 2 + 1]


    for i in range(M):
        node, value = map(int, input().split())
        ans[node] = value

    perfect(1)
    print('#{} {}'.format(tc, ans[L]))