import sys

sys.stdin = open('파스칼_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())

    tri = [([1] + [0] * (N - 1)) for _ in range(N)]

    for i in range(1, N):
        for j in range(1, N):
            tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]

    print('#{}'.format(tc))
    for x in range(N):
        print(*tri[x][:x+1])