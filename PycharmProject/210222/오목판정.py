import sys

sys.stdin = open('오목판정_input.txt', 'r')


def five_check(r, c):
    dr = [1, 0, 1, 1]
    dc = [0, 1, 1, -1]

    for d in range(4):
        cnt = 0
        tmp_r = r
        tmp_c = c
        while 0 <= tmp_r < N and 0 <= tmp_c < N:
            if my_map[tmp_r][tmp_c] == 'o':
                cnt += 1

                if cnt == 5:
                    return True
                tmp_r += dr[d]
                tmp_c += dc[d]

            elif my_map[tmp_r][tmp_c] == '.':
                cnt = 0
                tmp_r += dr[d]
                tmp_c += dc[d]

    return False


for tc in range(1, int(input()) + 1):
    N = int(input())
    my_map = [list(input()) for _ in range(N)]
    result = 0
    print('#{}'.format(tc), end=' ')

    for i in range(N):
        for j in range(N):
            if my_map[i][j] == 'o':
                if five_check(i, j):
                    result = 1

    if result == 1:
        print('YES')
    else:
        print('NO')
