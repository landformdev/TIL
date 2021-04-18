# 1
# 1 1 1 1
# 1 1 1 2
# 1 1 2 1
# 1 1 1 1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def check(number, cnt, r, c):
    if cnt == 6:
        result.add(number)
        return

    for n in range(4):
        nr = r + dr[n]
        nc = c + dc[n]

        if nr < 0 or nc < 0 or nr > 3 or nc > 3:
            continue

        check(number + str(my_map[nr][nc]), cnt + 1, nr, nc)


for tc in range(1, int(input()) + 1):
    my_map = [list(map(int, input().split())) for _ in range(4)]

    result = set()

    for i in range(4):
        for j in range(4):
            check(str(my_map[i][j]), 0, i, j)
    # for row in result:
    #     print(row)
    print('#{} {}'.format(tc, len(result)))
