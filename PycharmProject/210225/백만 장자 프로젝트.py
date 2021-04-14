import sys

sys.stdin = open('백만장자_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    earn = 0

    ###########################런타임 에러 남################################
    # while prices != []:  # 더이상 볼게 없을때까지 반복
    #
    #     # 최대값의 앞까지 잘라서 더한후 (최대값)*(앞의 값의 수)에서 빼서 계산
    #     # 남은 뒷부분을 이용해 계산 반복
    #     max_value = max(prices)
    #
    #     max_idx = prices.index(max_value)
    #
    #     mintomaxlist = prices[:max_idx]
    #
    #     earn += len(mintomaxlist)*max_value - sum(mintomaxlist)
    #
    #     prices = prices[max_idx+1:]
    ###########################################################################
    max_val = 0
    cnt = 0
    sum_lst = 0

    for i in range(N - 1, -1, -1):
        if prices[i] > max_val:

            earn += cnt * max_val
            earn -= sum_lst
            cnt = 0
            sum_lst = 0

            max_val = prices[i]


        elif prices[i] < max_val:
            cnt += 1
            sum_lst += prices[i]

        if i == 0:
            earn += cnt * max_val
            earn -= sum_lst

    print('#{} {}'.format(tc, earn))
