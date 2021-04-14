import sys

sys.stdin = open('반복문자_input.txt', 'r')


for tc in range(1, int(input()) + 1):
    s = list(input())

    lst = [0]  # 인덱스 오류 방지용
    # s를 탐색
    for i in s:
        if lst[-1] != i:  # top값과 들어올 값이 다르면 lst에 추가
            lst.append(i)
        else:  # 같으면 top값 pop
            lst.pop()

    # 앞의 0값 제외
    ans = len(lst)-1

    print('#{} {}'.format(tc, ans))