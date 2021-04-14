import sys

sys.stdin = open('간단한소인수분해_input.txt', 'r')

T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     numbers = [2, 3, 5, 7, 11]
#     abcde = []
#     for num in numbers:
#         cnt = 0
#         while True:
#             if N % num != 0:
#                 break
#             else:
#                 N = N / num
#                 cnt += 1
#
#         abcde.append(cnt)  # 리스트를 띄어쓰기 형태로 못바꿀까??

a, b, c, d, e = 0, 0, 0, 0, 0

for tc in range(1, T+1):
    N = int(input())

    cnt = 0
    while True:
        if N % 2 != 0:
            break
        else:
            N = N / 2
            cnt += 1
    a = cnt

    cnt = 0
    while True:
        if N % 3 != 0:
            break
        else:
            N = N / 3
            cnt += 1
    b = cnt

    cnt = 0
    while True:
        if N % 5 != 0:
            break
        else:
            N = N / 5
            cnt += 1
    c = cnt

    cnt = 0
    while True:
        if N % 7 != 0:
            break
        else:
            N = N / 7
            cnt += 1
    d = cnt

    cnt = 0
    while True:
        if N % 11 != 0:
            break
        else:
            N = N / 11
            cnt += 1
    e = cnt

    print('#{} {} {} {} {} {}'.format(tc, a, b, c, d, e))
