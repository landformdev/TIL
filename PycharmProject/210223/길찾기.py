import sys
sys.stdin = open('길찾기_input.txt', 'r')

# 재귀 DFS
def dfs(v):
    visited[v] = True
    route.append(v)

    for w in range(100):
        if my_map[v][w] and visited[w] != 1:
            dfs(w)


for _ in range(1, 11):
    tc, E = map(int, input().split())

    # 100x100 인접행렬틀 생성
    my_map = [[0]*100 for _ in range(100)]

    E_list = list(map(int, input().split()))

    # 인접행렬 생성
    for i in range(0, E*2, 2):
        my_map[E_list[i]][E_list[i+1]] = 1

    # 방문 체크
    visited = [False]*100

    # 경로 담을 리스트
    route = []

    dfs(0)

    # 99(종점)을 지나는 경우 1
    print('#{}'.format(tc), end=' ')
    if 99 in route:
        print(1)
    else:
        print(0)