import sys

sys.stdin = open('미로2_input.txt', 'r')

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]


def bfs(r, c):
    Q = [0] * 100000

    front, rear = -1, -1
    rear += 1
    Q[rear] = (r, c)

    visited[r][c] = 1

    while front != rear:
        front += 1
        crr_r, crr_c = Q[front]

        if miro[crr_r][crr_c] == 3:
            return 1

        for d in range(4):
            nr = crr_r + dr[d]
            nc = crr_c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if miro[nr][nc] != 1 and visited[nr][nc] != 1:
                rear += 1
                visited[nr][nc] = 1
                Q[rear] = (nr, nc)

    return 0


for tc in range(10):
    tc = int(input())
    N = 100

    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                ans = bfs(i, j)
                print('#{} {}'.format(tc, ans))
