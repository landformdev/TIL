import sys

sys.stdin = open('계산기2_input.txt', 'r')

for tc in range(1, 11):
    N = int(input())

    string = input()

    ###########후위표기#################

    operator = ['+', '-', '*', '/', '(', ')']

    stack = ['X']  # 인덱스 에러 방지용

    result = []  # 후위표기 담을 그릇

    for i in string:
        if i not in operator:
            result.append(i)

        elif i == '(':
            stack.append(i)

        elif i == ')':
            while stack[len(stack) - 1] != '(':
                result.append(stack.pop())
            stack.pop()

        elif i == '+' or i == '-':
            while stack[len(stack) - 1] == '+' or stack[len(stack) - 1] == '-' or stack[len(stack) - 1] == '*' or stack[len(stack) - 1] == '/':
                result.append(stack.pop())
            stack.append(i)

        elif i == '*' or i == '/':
            while stack[len(stack) - 1] == '*' or stack[len(stack) - 1] == '/':
                result.append(stack.pop())
            stack.append(i)

    while stack[len(stack) - 1] == '+' or stack[len(stack) - 1] == '-' or stack[len(stack) - 1] == '*' or stack[len(stack) - 1] == '/':
        result.append(stack.pop())

    ############연산#####################

    ans = []  # 연산 과정을 진행하고 결과값을 남길 그릇

    for j in result:
        if j not in operator:
            ans.append(j)

        else:
            A = int(ans.pop())
            B = int(ans.pop())

            if j == '-':
                ans.append(B - A)
            if j == '+':
                ans.append(B + A)
            if j == '*':
                ans.append(B * A)
            if j == '/':
                ans.append(B / A)

    print('#{}'.format(tc), end=' ')
    print(*ans)
