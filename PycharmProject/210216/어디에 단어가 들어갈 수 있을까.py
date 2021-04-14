import sys

sys.stdin = open('어디에이단어가_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())

    num_map = [list(map(int, input().split())) + [0] for _ in range(N)]

    num_map.append([0] * N)

    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if num_map[i][j] == 1:
                cnt += 1
            else:
                cnt = 0

            if cnt == K and num_map[i][j + 1] == 0:
                cnt = 0
                ans += 1

    for l in range(N):
        cnt = 0
        for k in range(N):
            if num_map[k][l] == 1:
                cnt += 1
            else:
                cnt = 0

            if cnt == K and num_map[k + 1][l] == 0:
                cnt = 0
                ans += 1

    print('#{} {}'.format(tc, ans))
