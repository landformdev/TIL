import sys

sys.stdin = open('sum_input.txt', 'r')

for tc in range(1, 11):
    arr = []
    num = int(input())
    for n in range(100):
        arr.append(list(map(int, input().split())))

    sum_list = []
    cross_tmp = 0
    cross_tmp2 = 0
    for i in range(100):
        row_tmp = 0
        col_tmp = 0
        cross_tmp += arr[i][i]
        cross_tmp2 += arr[i][99-i]
        for j in range(100):
            row_tmp += arr[i][j]
            col_tmp += arr[j][i]
        sum_list.append(row_tmp)
        sum_list.append(col_tmp)
    sum_list.append(cross_tmp)
    sum_list.append(cross_tmp2)

    max_value = 0
    for k in sum_list:
        if max_value < k:
            max_value = k

    print('#{} {}'.format(num, max_value))







