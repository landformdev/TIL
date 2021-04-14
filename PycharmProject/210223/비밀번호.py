import sys
sys.stdin = open('비밀번호_input.txt', 'r')

for tc in range(1, 11):
    N, string = map(str, input().split())

    result = ['x']  # 혹시모를 인덱스 오류 대비
    for i in string:

        if i == result[-1]:
            result.pop()

        else:
            result.append(i)

    print('#{} {}'.format(tc, ''.join(result[1:])))