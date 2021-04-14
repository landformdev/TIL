def bfs(sV):
    Q = [(sV, 0)]
    visited = [0] * (V + 1)
    visited[sV] = 1

    while Q:
        v, dist = Q.pop(0)

        if v == eV:
            return dist

        for i in range(1, V + 1):
            if adj_arr[v][i] == 1 and visited[i] == 0:
                Q.append([i, dist + 1])
                visited[i] = True

    return 0

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    adj_arr = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        a, b = map(int, input().split())
        adj_arr[a][b] = 1
        adj_arr[b][a] = 1

    sV, eV = map(int, input().split())

    print('#{} {}'.format(tc, bfs(sV)))
