# for tc in range(1, int(input())+1):
# F801FF801FF801F003FF003E0003E0FFC1FFFC1FF83E0FFFFF003E007FE0FFC0007C


for tc in range(1, int(input()) + 1):

    sixteen = input()

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
    print(len(result))

11111000000000011111111110000000000111111111100000000001111100000000001111111111000000000011111000000000000000111110000011111111110000011111111111111100000111111111100000111110000011111111111111111111000000000011111000000000011111111110000011111111110000000000000001111100
