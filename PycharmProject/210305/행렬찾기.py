import sys
sys.stdin = open('행렬찾기_input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def garosero(r, c):
    global cnt_c, cnt_r
    container[r][c] = 0
    cnt_c = 1
    while True:
        if c + 1 > n - 1:
            break
        if container[r][c + 1] == 0:
            break
        c += 1
        container[r][c] = 0
        cnt_c += 1

    cnt_r = 1
    while True:
        if r + 1 > n - 1:
            break
        if container[r + 1][c] == 0:
            break
        r += 1
        container[r][c] = 0
        cnt_r += 1

    rc_lst.append((cnt_r, cnt_c, cnt_c * cnt_r))


def make_zero(zero_r, zero_c):
    for n in range(zero_r + 1, zero_r + cnt_r):
        for m in range(zero_c, zero_c + cnt_c - 1):
            container[n][m] = 0


for tc in range(1, int(input()) + 1):
    n = int(input())
    container = [list(map(int, input().split())) for _ in range(n)]

    rc_lst = []
    for i in range(n):
        for j in range(n):
            if container[i][j] != 0:
                garosero(i, j)
                make_zero(i, j)

    ans_lst = sorted(rc_lst, key=lambda x: (x[2], x[0]))

    print('#{} {}'.format(tc, len(ans_lst)), end=' ')
    for num in ans_lst:
        print(num[0], num[1], end=' ')
    print()
