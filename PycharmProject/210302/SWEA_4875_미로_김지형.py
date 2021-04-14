import sys

sys.stdin = open('미로_input.txt', 'r')


dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]


def dfs(r, c):
    global ans
    visited[r][c] = 1

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        if miro[nr][nc] == 3:
            ans = 1
            return

        if miro[nr][nc] == 1:
            continue
        if visited[nr][nc] == 1:
            continue

        dfs(nr, nc)


for tc in range(3):
    tc = int(input())
    N = 5

    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                dfs(i, j)
                print('#{} {}'.format(tc, ans))
