# def check(i, n):
#     global min_battery
#     if i == n:
#         s = 0
#         for j in range(1, n):
#             s += golf_map[route[j-1]][route[j]]
#             if min_battery < s:
#                 return
#         s += golf_map[route[n-1]][0]
#
#         if min_battery > s:
#             min_battery = s
#     else:
#         for j in range(n):
#             if v[j] == 0:
#                 v[j] = 1
#                 route[i] = j
#                 check(i+1, n)
#                 v[j] = 0
#
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     golf_map = [list(map(int, input().split())) for _ in range(N)]
#
#     route = [0]*N
#     v = [0]*N
#     v[0] = 1
#     min_battery = 99999999
#
#     check(1, N)
#     print('#{} {}'.format(tc, min_battery))


def check(i, n, s):
    global min_battery
    if i == n:
        s += golf_map[route[n-1]][0]

        if min_battery > s:
            min_battery = s
    else:
        for j in range(n):
            if v[j] == 0:
                v[j] = 1
                route[i] = j
                check(i+1, n, s + golf_map[route[i-1]][j])
                v[j] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    golf_map = [list(map(int, input().split())) for _ in range(N)]

    route = [0]*N
    v = [0]*N
    v[0] = 1
    min_battery = 99999999

    check(1, N, 0)
    print('#{} {}'.format(tc, min_battery))