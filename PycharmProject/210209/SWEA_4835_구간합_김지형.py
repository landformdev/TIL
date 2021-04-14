import sys

sys.stdin = open('구간합_input.txt', 'r')

test_case = int(input())

for tc in range(test_case):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    arr_sums = []

    for n in range(N - M + 1):
        arr_sum = 0
        for m in range(M):
            arr_sum += arr[m + n]

        arr_sums.append(arr_sum)

    for i in range(len(arr_sums) - 1, 0, -1):
        for j in range(i):
            if arr_sums[j] > arr_sums[j + 1]:
                arr_sums[j], arr_sums[j + 1] = arr_sums[j + 1], arr_sums[j]

    print('#{} {}'.format(tc + 1, arr_sums[-1] - arr_sums[0]))

    #################################################################
    max_value = 0
    min_value = 987654321

    # 구간시작점
    for i in range(N - M + 1):
        tmp = 0

        for j in range(M):
            tmp += arr[i + j]

        # for j in arr[i:i+M]:
        #     tmp += j

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print(max_value - min_value)

    ### 중복된 연산 피하기! 윈도우 슬라이드 방식 ########################

    # 첫 구간은 구해놓자
    tmp = 0
    for i in range(M):
        tmp += arr[i]

    max_value = tmp
    min_value = tmp

    for i in range(M, N):
        # 새로운 구간의 합을 아주아주 간단하게 구할 수 있다.
        tmp = tmp + arr[i] - arr[i - M]

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print(max_value - min_value)
