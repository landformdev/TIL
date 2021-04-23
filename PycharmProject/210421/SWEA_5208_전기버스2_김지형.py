# def BUS(num):
#     global cnt, result
#
#     if num >= N:
#         if result > cnt:
#             result = cnt
#         return
#
#     if result < cnt:
#         return
#
#     start = num
#     life = Data[start]
#
#     for i in range(start + life, start, -1):
#         cnt += 1
#         BUS(i)
#         cnt -= 1
#
#
# for tc in range(1, int(input()) + 1):
#     Data = list(map(int, input().split()))
#     N = Data[0]
#     result = 9999999
#     cnt = 0
#
#     BUS(1)
#
#     print('#{} {}'.format(tc, result - 1))

