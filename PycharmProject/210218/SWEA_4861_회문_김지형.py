import sys
sys.stdin = open('회문_input.txt', 'r')


# # 펠린드롬이면 True 아니면 False
# def palin_check(x):
#     copy_x = x[:]
#     for i in range(len(x) // 2):
#         x[i], x[len(x) - 1 - i] = x[len(x) - 1 - i], x[i]
#     if x == copy_x:
#         return True
#     else:
#         return False
#
#
# for tc in range(1, int(input()) + 1):
#
#     N, M = map(int, input().split())
#
#     # 문자를 받아와 NxN 글자판 생성
#     my_map = [[] for _ in range(N)]
#     for n in range(N):
#         my_map[n] = list(input())
#
#     # 테스트 케이스 출력
#     print('#{}'.format(tc), end=' ')
#
#     # 가로방향에서 회문 검색 후 출력
#     string1 = []
#     for i in range(N):
#         for j in range(N - M + 1):
#             string1 = my_map[i][j:M + j]
#
#             if palin_check(string1):
#                 print(''.join(string1))
#
#             # 세로방향에서 회문 검색 후 출력
#             string2 = []
#             for k in range(j, j + M):
#                 string2.append(my_map[k][i])
#
#             if palin_check(string2):
#                 print(''.join(string2))
#


################################################################################################

