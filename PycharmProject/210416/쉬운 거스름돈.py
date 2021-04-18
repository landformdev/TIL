for tc in range(1, int(input())+1):
    money_unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0]*8

    money = int(input())

    # for i in range(8):
    #     while money >= money_unit[i]:
    #         money = money - money_unit[i]
    #         result[i] += 1
    for i in range(8):
        if money >= money_unit[i]:
            result[i] = money // money_unit[i]
            money %= money_unit[i]

    print('#{}\n{}'.format(tc, ' '.join(map(str, result))))


