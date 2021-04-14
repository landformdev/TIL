import sys

sys.stdin = open('gravity_input.txt', 'r')

# def BubbleSort(a):
#     for i in range(len(a)-1, 0 , -1):
#         for j in range(i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
#
# test_case = int(input())
#
# for tc in range(test_case):
#     N = int(input())
#     boxs = list(map(int, input().split()))
#
#     origin_box = boxs[:]
#     cnt = 0
#     lst = []
#
#     for box in origin_box:
#         cnt2 = 0
#         for droped in BubbleSort(boxs):
#             if box == droped and BubbleSort(boxs)[cnt2] != BubbleSort(boxs)[cnt2-1]:
#                 lst.append(cnt2 - cnt)
#             cnt2 += 1
#         cnt += 1
#
#     print('#{} {}'.format(tc + 1, BubbleSort(lst)[-1]))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))

# 전체 모든 박스 해보기
    ans = 0
    for i in range(len(box)):
        cnt = 0
        # 나 다음부터 나보다 작은 값을 찾아 카운트
        for j in range(i+1, len(box)):
            if box[i] > box[j]:
                cnt += 1

        if ans < cnt:
            ans = cnt

    print('#{} {}'.format(tc, ans))
