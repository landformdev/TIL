# import sys
# sys.stdin = open('forth_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    string = list(input().split())

    stack = []  # 스택

    ans = 'error'  # 결과값이 안나오면 error

    operator = ['+', '-', '/', '*']  # 연산자 리스트

    cnt = 0

    for i in string:
        # . 이 1개 이상 나올경우 체크
        if i == '.':
            cnt += 1
        # 연산자 리스트가 아니면 스택에 추가
        if i not in operator:
            stack.append(i)
        # 연산할게 없으면 break 후 error 출력
        elif len(stack) < 2:
            break
        # 연산자별로 계산
        elif i == '+':
            A = int(stack.pop())
            B = int(stack.pop())
            stack.append(B + A)
        elif i == '-':
            A = int(stack.pop())
            B = int(stack.pop())
            stack.append(B - A)
        elif i == '/':
            A = int(stack.pop())
            B = int(stack.pop())
            stack.append(B / A)
        elif i == '*':
            A = int(stack.pop())
            B = int(stack.pop())
            stack.append(B * A)
        # 마지막에 stack에 최종값과 .만 있으면 값 출력
        if stack[-1] == '.' and len(stack) == 2 and cnt == 1:
            ans = int(stack[0])

    print('#{} {}'.format(tc, ans))
