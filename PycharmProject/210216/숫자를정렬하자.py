for tc in range(1, int(input())+1):
    N = int(input())
    raw_list = list(map(int, input().split()))

    for i in range(0, N-1):
        min = i
        for j in range(i+1, N):
            if raw_list[min] > raw_list[j]:
                min = j
        raw_list[min], raw_list[i] = raw_list[i], raw_list[min]

    print('#{} {}'.format(tc, ' '.join(map(str, raw_list))))
