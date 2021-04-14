import sys
sys.stdin = open('의석이_input.txt', 'r')


for tc in range(1, int(input())+1):

    # 문자 받아와서 2차원 배열 구성
    my_map = [list(input()) for _ in range(5)]

    # 가장 긴 행의 길이 구하기
    max_leng = 0
    for leng in my_map:
        if len(leng) > max_leng:
            max_leng = len(leng)

    # 답을 담을 상자
    ans = ''

    # 세로로 읽으면서 문자 추출하고 행의 문자열보다 길면 건너뛰기
    for i in range(max_leng):
        for j in range(5):
            if i > len(my_map[j])-1:
                continue
            ans += my_map[j][i]

    print('#{} {}'.format(tc, ans))