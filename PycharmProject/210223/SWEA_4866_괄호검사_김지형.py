import sys

sys.stdin = open('괄호검사_input.txt', 'r')

for tc in range(1, int(input()) + 1):

    lst = list(input())  # 문자열 리스트
    check = [0]  # 괄호를 담으며 체크해볼 리스트 (인덱스 에러를 막기위해 0 넣음)
    left_cnt = 0  # 왼쪽괄호 갯수
    right_cnt = 0  # 오른쪽괄호 갯수

    for i in lst:
        # 오른쪽 괄호 카운트
        if i == ']' or i == '}' or i == ')':
            right_cnt += 1
        # 왼쪽 괄호 카운트 & ckeck리스트에 추가
        if i == '[' or i == '{' or i == '(':
            left_cnt += 1
            check.append(i)

        # 들어있는 왼쪽괄호와 읽은 오른쪽 괄호가 같으면 pop
        if check[-1] == '[' and i == ']':
            check.pop()

        if check[-1] == '{' and i == '}':
            check.pop()

        if check[-1] == '(' and i == ')':
            check.pop()

    print('#{}'.format(tc), end=' ')
    # 괄호의 쌍이 맞아 전부 pop되고 그 갯수또한 같으면 1 아님 0
    if check == [0] and left_cnt == right_cnt:
        print(1)
    else:
        print(0)
