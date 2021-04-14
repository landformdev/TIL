import sys

sys.stdin = open('ladder2_input.txt', 'r')


def copy(x):
    result = []
    for i in x:
        new = i[:]
        result.append(new)
    return result


for tc in range(1, 11):
    tc = int(input())

    my_map = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    min_cnt = 99999999999
    min_cnt_ans = 0
    for i in range(1, 101):
        copy_map = copy(my_map)
        j = 0

        if my_map[j][i] == 1:
            ans = i
            cnt = 0
            while j != 99:

                if copy_map[j][i + 1] == 1:
                    copy_map[j][i] = 0
                    i += 1
                    cnt += 1

                if copy_map[j][i - 1] == 1:
                    copy_map[j][i] = 0
                    i -= 1
                    cnt += 1

                if copy_map[j][i] == 1 and copy_map[j][i + 1] == 0 and copy_map[j][i - 1] == 0:
                    copy_map[j][i] = 0
                    j += 1
                    cnt += 1

            if cnt < min_cnt:
                min_cnt = cnt
                min_cnt_ans = ans

    print('#{} {}'.format(tc, min_cnt_ans - 1))
