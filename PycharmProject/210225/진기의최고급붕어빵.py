# import sys
#
# sys.stdin = open('진기붕어빵_input.txt', 'r')

for tc in range(1, int(input()) + 1):

    N, M, K = map(int, input().split())

    seconds = list(map(int, input().split()))

    scd = sorted(seconds)

    cnt = -1
    fishbread = 0

    print('#{}'.format(tc), end=' ')
    while True:
        cnt += 1
        if cnt % M == 0 and cnt > 0:
            fishbread += K

        for i in scd:
            if i == cnt:
                fishbread -= 1

        if fishbread < 0:
            print('Impossible')
            break
        if cnt > scd[-1]:
            print('Possible')
            break
