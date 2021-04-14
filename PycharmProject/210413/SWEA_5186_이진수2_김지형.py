for tc in range(1, int(input()) + 1):

    num = float(input())  # 소수니까 float로 받기
    result = []

    while True:
        num *= 2
        # 두배 한 값이 1보다 크면 1 저장 후 -1
        if num > 1:
            num -= 1
            result.append(1)
        # 두배 한 값이 1이면 1 저장 후 종료
        elif num == 1:
            result.append(1)
            break
        # 1보다 작으면 0 저장
        else:
            result.append(0)

        # 13개 이상은 overflow이므로 필요없음
        if len(result) > 12:
            break

    print('#{}'.format(tc), end=' ')
    if len(result) > 12:
        print('overflow')
    else:
        print(''.join(map(str, result)))
