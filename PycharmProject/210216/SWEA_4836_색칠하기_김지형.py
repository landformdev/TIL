import sys

sys.stdin = open('색칠하기_input.txt', 'r')

for tc in range(1, int(input())+1):

    my_map = [[0]*10 for _ in range(10)]

    color_info = []
    cnt = 0
    for n in range(int(input())):
        color_info.append(list(map(int, input().split())))

        for i in range(color_info[n][1], color_info[n][3]+1):
            for j in range(color_info[n][0], color_info[n][2]+1):
                my_map[j][i] += color_info[n][4]
                if my_map[j][i] == 3:
                    cnt += 1

    print('#{} {}'.format(tc, cnt))
