import sys

sys.stdin = open('오셀로_input.txt', 'r')

for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())

    my_map = [[0] * (N + 1) for _ in range(N + 1)]

    default = N // 2
    my_map[default + 1][default] = 1
    my_map[default][default + 1] = 1
    my_map[default][default] = 2
    my_map[default + 1][default + 1] = 2

    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for _ in range(M):
        x, y, color = map(int, input().split())
        tmp_x = x
        tmp_y = y
        my_map[y][x] = color

        for d in range(8):
            step = 0
            x = tmp_x
            y = tmp_y
            while 0 < y + dr[d] <= N and 0 < x + dc[d] <= N:
                if my_map[y + dr[d]][x + dc[d]] != color and my_map[y + dr[d]][x + dc[d]] != 0:

                    x += dc[d]
                    y += dr[d]
                    step += 1

                elif my_map[y + dr[d]][x + dc[d]] == color and step >= 1:
                    for s in range(step):
                        my_map[y][x] = color
                        x -= dc[d]
                        y -= dr[d]
                    break
                else:
                    break

    cnt_b = 0
    cnt_w = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if my_map[i][j] == 1:
                cnt_b += 1
            if my_map[i][j] == 2:
                cnt_w += 1

    print('#{} {} {}'.format(tc, cnt_b, cnt_w))


