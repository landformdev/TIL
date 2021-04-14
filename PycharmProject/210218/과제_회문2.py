import sys
sys.stdin = open('회문2_input.txt', 'r')

# # 회문1의 코드를 응용함
#
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
# for tc in range(1, 11):
#     tc = int(input())
#
#     # 문자를 받아와 100x100 글자판 생성
#     my_map = [[] for _ in range(100)]
#     for n in range(100):
#         my_map[n] = list(input())
#
#     # 테스트 케이스 출력
#     print('#{}'.format(tc), end=' ')
#
#
#     string1 = []  # 가로검색을 위한 빈 리스트
#     max_length = 0
#     for i in range(100):
#         for M in range(1, 101):  # 1~100까지의 문자열 체크
#             # max_length보다 작은 길이는 시행하지 않음
#             if max_length > M:
#                 continue
#
#             # 가로방향에서 회문 검색 후 출력
#             for j in range(100 - M + 1):
#                 string1 = my_map[i][j:M + j]
#
#                 if palin_check(string1) and len(string1) > max_length:
#                     max_length = len(string1)
#
#                 # 세로방향에서 회문 검색 후 출력
#                 string2 = []  # 세로검색을 위한 빈 리스트
#                 for k in range(j, j + M):
#                     string2.append(my_map[k][i])
#
#                 if palin_check(string2) and len(string2) > max_length:
#                     max_length = len(string2)
#
#     print(max_length)


##########################실행시간을 더 줄이려면?#################################################

# 펠린드롬이면 True 아니면 False
def palin_check(x):
    copy_x = x[:]
    for i in range(len(x) // 2):
        x[i], x[len(x) - 1 - i] = x[len(x) - 1 - i], x[i]
    if x == copy_x:
        return True
    else:
        return False


for tc in range(1, 11):
    tc = int(input())

    # 문자를 받아와 100x100 글자판 생성
    my_map = [[] for _ in range(100)]
    for n in range(100):
        my_map[n] = list(input())

    # 테스트 케이스 출력
    print('#{}'.format(tc), end=' ')

    # 가로방향에서 회문 검색 후 출력
    string1 = []  # 가로검색을 위한 빈 리스트
    for i in range(100):
        for M in range(100, -1, -1):  # 100~1까지 역순으로 문자열 체크
            for j in range(100 - M + 1):
                string1 = my_map[i][j:M + j]

                if palin_check(string1):
                    garo = len(string1)
                    break


    # 세로방향에서 회문 검색 후 출력
    string2 = []  # 세로검색을 위한 빈 리스트
    for i in range(100):
        for M in range(100, -1, -1):
            for j in range(100 - M + 1):
                for k in range(j, j + M):
                    string2.append(my_map[k][i])

                if palin_check(string2):
                    sero = len(string2)
                    break


    if garo >= sero:
        print(garo)

    else:
        print(sero)

