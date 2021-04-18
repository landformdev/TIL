dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def search(r, c):
    cnt = 1
    room = rooms[r][c]
    while True:
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if not (0 <= nr < N and 0 <= nc < N and rooms[nr][nc] - rooms[r][c] == 1): continue
            cnt += 1
            r, c = nr, nc
            break
        else:
            return room, cnt


for tc in range(1, int(input()) + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    num = []

    for i in range(N):
        for j in range(N):
            n, c = search(i, j)
            if c > max_cnt:
                num = [n]
                max_cnt = c
            elif c == max_cnt:
                num.append(n)

    num.sort()
    print("#{} {} {}".format(tc, num[0], max_cnt))