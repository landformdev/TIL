import sys

sys.stdin = open('농작물수확_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())

    farm_map = [list(map(int, input())) for _ in range(N)]

    mid = N // 2
    harvest = 0

    for i in range(N):
        if i <= mid:
            for j in range(mid - i, mid + i + 1):
                harvest += farm_map[i][j]
        if i > mid:
            for j in range(i - mid, N - i + mid):
                harvest += farm_map[i][j]

    print('#{} {}'.format(tc, harvest))
