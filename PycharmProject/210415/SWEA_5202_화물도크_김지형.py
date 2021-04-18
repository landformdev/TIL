for tc in range(1, int(input()) + 1):
    N = int(input())

    apps = [list(map(int, input().split())) for _ in range(N)]

    apps.sort(key=lambda x: x[1])
    max_dock = [apps[0][0]]

    for i in range(N):
        if apps[i][0] >= max_dock[len(max_dock) - 1]:
            max_dock.append(apps[i][1])
    # for row in apps:
    #     print(row)
    # print(max_dock)
    print('#{} {}'.format(tc, len(max_dock) - 1))

# 1
# 15
# 18 19
# 2 7
# 11 15
# 13 16
# 23 24
# 2 14
# 13 22
# 20 23
# 13 19
# 7 15
# 5 21
# 20 24
# 16 22
# 17 21
# 9 24
