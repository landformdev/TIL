for tc in range(1, int(input()) + 1):

    N, sixteen = input().split()

    # 인덱스값을 이용하기 위한 것
    hexadecimal = '0123456789ABCDEF'

    result = ''

    for i in sixteen:
        # 인덱스로 문자를 숫자로 변환
        num = hexadecimal.index(i)
        for j in range(3, -1, -1):
            # 16진수를 2진수로 변환
            result += '1' if num & (1 << j) else '0'

    print('#{} {}'.format(tc, result))
