for tc in range(1, int(input())+1):

    N = int(input())


    shape_cnt = 0

    shape_cnt += 1  # 모두 10일때

    num_10 = int(N / 10)  # 한번에 들어갈 수 있는 10*20 갯수

    num_20 = int(N // 20)  # 한번에 들어갈 수 있는 20*20 갯수


    #팩토리얼 함수
    def fa(x):
        ans = 1
        for k in range(1, x + 1):
            ans *= k
        return ans


    for i in range(1, num_20 + 1):
        # 식을통해 갯수를 구해 더한다
        shape_cnt += int(fa(num_10 - i) / (fa(i) * fa(num_10 - 2 * i)))*2**i

    print('#{} {}'.format(tc, shape_cnt))
