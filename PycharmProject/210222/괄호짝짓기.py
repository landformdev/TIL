import sys

sys.stdin = open('괄호짝짓기_input.txt', 'r')

for tc in range(1, 11):
    N = int(input())

    lst = list(input())
    check_list = []
    left = ['<', '[', '{', '(']
    cnt_left = 0
    cnt_right = 0
    for i in lst:

        if i in left:
            check_list.append(i)
            cnt_left += 1
        else:
            cnt_right += 1

        if i == '>' and check_list[-1] == '<':
            check_list.pop()

        if i == '}' and check_list[-1] == '{':
            check_list.pop()

        if i == ']' and check_list[-1] == '[':
            check_list.pop()

        if i == ')' and check_list[-1] == '(':
            check_list.pop()

    print('#{}'.format(tc), end=' ')
    if cnt_right != cnt_left:
        print(0)
    elif check_list == []:
        print(1)
    else:
        print(0)
