for tc in range(1, int(input())+1):
    N = int(input())
    ans = [0]
    def perfect(n):
        if n*2 <= N:
            perfect(n*2)
        ans.append(n)
        if n*2+1 <= N:
            perfect(n*2+1)


    perfect(1)  # 인덱스가 노드의 값이고 리스트의 값이 노드번호인 리스트 생성
    for i in range(1, N+1):
        if ans[i] == 1:
            root = i
        if ans[i] == N//2:
            half = i

    print('#{} {} {}'.format(tc, root, half))