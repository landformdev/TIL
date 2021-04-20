# 인덱스 이용하자
def separate(lst):
    M = len(lst) // 2
    if len(lst) == 1:
        return lst

    left = lst[:M]
    right = lst[M:]

    left = separate(left)
    right = separate(right)

    return merge(left, right)


def merge(left_list, right_list):
    global cnt

    result = [0] * (len(left_list) + len(right_list))  # 리스트의 길이 주의하자
    result_idx = 0
    left_idx = 0
    right_idx = 0

    if left_list[- 1] > right_list[- 1]:
        cnt += 1

    while len(left_list) > left_idx and len(right_list) > right_idx:

        if left_list[left_idx] <= right_list[right_idx]:

            # print(result, left_list, right_list, result_idx, left_idx, result_idx)

            result[result_idx] = left_list[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right_list[right_idx]
            right_idx += 1
        result_idx += 1

    while len(left_list) > left_idx:
        result[result_idx] = left_list[left_idx]
        left_idx += 1
        result_idx += 1

    while len(right_list) > right_idx:
        # print('오냐',result, left_list, right_list, result_idx, left_idx, result_idx)
        result[result_idx] = right_list[right_idx]
        right_idx += 1
        result_idx += 1

    return result


for tc in range(1, int(input()) + 1):
    N = int(input())
    L = list(map(int, input().split()))

    cnt = 0

    print('#{} {} {}'.format(tc, separate(L)[N // 2], cnt))

################################ 시간초과 ###########################

# def separate(lst):
#     M = len(lst) // 2
#     if len(lst) == 1:
#         return lst
#
#     left = lst[:M]
#     right = lst[M:]
#
#     left = separate(left)
#     right = separate(right)
#
#     return merge(left, right)
#
#
# def merge(left_list, right_list):
#     result = []
#
#     global cnt
#
#     if left_list[len(left_list) - 1] > right_list[len(right_list) - 1]:
#         cnt += 1
#
#     while len(left_list) > 0 or len(right_list) > 0:
#
#         if len(left_list) > 0 and len(right_list) > 0:
#             if left_list[0] <= right_list[0]:
#                 result.append(left_list.pop(0))
#             else:
#                 result.append(right_list.pop(0))
#         elif len(left_list) > 0:
#             result.append(left_list.pop(0))
#         elif len(right_list) > 0:
#             result.append(right_list.pop(0))
#
#     return result
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#
#     L = list(map(int, input().split()))
#     cnt = 0
#
#     print('#{} {} {}'.format(tc, separate(L)[N // 2], cnt))
