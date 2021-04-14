import sys

sys.stdin = open('이진탐색_input.txt', 'r')

for tc in range(1, int(input())+1):
    P, Pa, Pb = map(int, input().split())

    l = 1
    r = P
    c = int((l+r)/2)
    a_cnt = 0
    b_cnt = 0

    while Pa != c:

        if Pa < c:
            r = c
            c = int((l + r) / 2)
        elif Pa > c:
            l = c
            c = int((l + r) / 2)

        a_cnt += 1


    l = 1
    r = P
    c = int((l+r)/2)

    while Pb != c:
        if Pb < c:
            r = c
            c = int((l + r) / 2)
        elif Pb > c:
            l = c
            c = int((l + r) / 2)

        b_cnt += 1

    print('#{}'.format(tc), end=' ')
    if a_cnt > b_cnt:
        print('B')
    elif a_cnt < b_cnt:
        print('A')
    else:
        print(0)