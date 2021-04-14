import sys

sys.stdin = open('특별정렬_input.txt', 'r')


def selsort(x):
    for n in range(0, len(x) - 1):
        min = n
        for m in range(n + 1, len(x)):
            if x[min] > x[m]:
                min = m
        x[n], x[min] = x[min], x[n]


for tc in range(1, int(input()) + 1):
    N = int(input())
    raw_list = list(map(int, input().split()))

    selsort(raw_list)

    ans_list = [0] * 10

    cnt = 1
    for i in range(0, N, 2):
        ans_list[i] = raw_list[N - cnt]
        ans_list[i + 1] = raw_list[cnt - 1]
        cnt += 1
        if cnt == 6:
            break

    print('#{} {}'.format(tc, ' '.join(map(str, ans_list))))
