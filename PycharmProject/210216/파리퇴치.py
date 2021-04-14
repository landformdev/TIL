import sys
sys.stdin = open('파리퇴치_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    fly_map = []
    for n in range(N):
        fly_map.append(list(map(int, input().split())))

    max_fly = 0

    for j in range(N-M+1):
        for i in range(N-M+1):
            flys = 0
            for k in range(M):
                for l in range(M):
                    flys += fly_map[i+l][j+k]

            if flys > max_fly:
                max_fly = flys

    print('#{} {}'.format(tc, max_fly))
