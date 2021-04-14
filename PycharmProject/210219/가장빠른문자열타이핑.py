import sys

sys.stdin = open('가장빠른타이핑_input.txt', 'r')

# 패턴검색해서 일치하는것 갯수 찾아냄
# def pattern_find(p, t):
#     ans = 0
#     for i in range(len(t)):
#         cnt = 0
#         for j in range(len(p)):
#             cnt += 1
#             if p[j] != t[i]:
#                 break
#             i += 1
#
#             if cnt == len(p):
#                 ans += 1
#     return ans

# 패턴검색해서 일치하는것 갯수 찾아냄
def pattern_find(p, t):
    i = 0
    j = 0
    cnt = 0
    while j < len(t):
        if p[i] != t[j]:
            j = j - i
            i = -1
        i += 1
        j += 1
        if i == len(p):
            i = 0
            cnt += 1
    return cnt


for tc in range(1, int(input()) + 1):
    A, B = input().split()

    N = pattern_find(B, A)

    # 전체 단어에서 겹치는 횟수만큼 제외 후 패턴의 수만큼 더함
    print('#{} {}'.format(tc, len(A) - len(B)*N + N))
