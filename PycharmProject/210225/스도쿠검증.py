import sys

sys.stdin = open('스도쿠검증_input.txt', 'r')


def test(x):
    for i in range(9):
        num_list = []
        for j in range(9):
            if x[i][j] in num_list:
                return 0
            num_list.append(x[i][j])

        num_list = []
        for j in range(9):
            if x[j][i] in num_list:
                return 0
            num_list.append(x[j][i])

    for r in range(0, 7, 3):
        for c in range(0, 7, 3):

            num_list = []
            for k in range(r, 3 + r):
                for l in range(c, 3 + c):
                    if x[k][l] in num_list:
                        return 0
                    num_list.append(x[k][l])
    return 1


for tc in range(1, int(input()) + 1):
    sudoku_map = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, test(sudoku_map)))
