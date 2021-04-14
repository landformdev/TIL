for tc in range(1, int(input())+1):

    cnt = 0  # 서브노드의 갯수
    def check(n):
        global cnt
        # 전위,후위, 중위 등 머든 써서 찍는 횟수 체크
        if n > 0:
            check(left[n])
            check(right[n])
            cnt += 1

        return cnt

    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    V = E + 1  # 정점의 수
    left = [0]*(V+1)
    right = [0]*(V+1)

    for i in range(V-1):
        pn, cn = tree[i*2], tree[i*2+1]
        if left[pn] == 0:
            left[pn] = cn
        else:
            right[pn] = cn

    check(N)
    print('#{} {}'.format(tc, cnt))
