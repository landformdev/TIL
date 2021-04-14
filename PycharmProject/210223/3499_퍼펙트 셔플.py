import sys

sys.stdin = open('퍼펙트셔플_input.txt', 'r')


def upp(x):
    if int(x) < x < x + 1:
        return int(x + 1)
    else:
        return x


for tc in range(1, int(input()) + 1):
    N = int(input())

    arr = input().split()

    suffled = [0] * N

    for i in range(0, N, 2):
        if i == 0:
            suffled[i] = arr[0]
        else:
            suffled[i] = arr[int(i / 2)]

    for j in range(1, N, 2):
        suffled[j] = arr[int(upp(N / 2) + (j - 1) / 2)]


    print('#{} {}'.format(tc, ' '.join(suffled)))

