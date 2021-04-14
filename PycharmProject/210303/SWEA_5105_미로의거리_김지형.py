import sys

sys.stdin = open('미로의 거리_input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def search():
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                return i, j


def BFS(r, c):
    # 선형큐를 써보자
    Q = [0] * 100000
    front, rear = -1, 0
    Q[rear] = (r, c)

    dist = [[-1] * (N) for _ in range(N)]
    dist[r][c] = 0

    # 선형큐에서 공백 검사
    while front != rear:
        front += 1
        curr_r, curr_c = Q[front]
        if miro[curr_r][curr_c] == '3':
            return dist[curr_r][curr_c] - 1
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if miro[nr][nc] != '1' and dist[nr][nc] == -1:
                dist[nr][nc] = dist[curr_r][curr_c] + 1
                rear += 1
                Q[rear] = (nr, nc)
    return 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    stR, stC = search()

    print(BFS(stR, stC))
