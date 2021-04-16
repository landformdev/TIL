dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

result = set()


def check(number, cnt, r, c):
    for n in range(4):
        nr = r + dr[n]
        nc = c + dc[n]

        if nr < 0 or nc < 0 or nr > 3 or nc > 3:
            continue
        cnt += 1
        number += str(my_map[nr][nc])

        if cnt == 6:
            result.add(number)
            return

        check(number, cnt, nr, nc)


for tc in range(1, int(input()) + 1):
    my_map = [list(map(int, input().split())) for _ in range(4)]

    for i in range(4):
        for j in range(4):
            check(str(my_map[i][j]), 0, i, j)
    for row in result:
        print(row)
    print('#{} {}'.format(tc, len(result)))
