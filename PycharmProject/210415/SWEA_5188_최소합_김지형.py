dr = [0, 1]
dd = [1, 0]


def minimum(r, d, n_sum):
    global mini

    n_sum += arr[r][d]

    if n_sum > mini:
        return

    for i in range(2):
        nr = r + dr[i]
        nd = d + dd[i]
        # 필터
        if nr > N - 1 or nr < 0 or nd > N - 1 or nd < 0:
            continue
        # 마지막 도달
        if nr == N - 1 and nd == N - 1:
            n_sum += arr[nr][nd]
            if n_sum < mini:
                mini = n_sum

            return

        minimum(nr, nd, n_sum)


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mini = 9999999999

    minimum(0, 0, 0)

    print('#{} {}'.format(tc, mini))
