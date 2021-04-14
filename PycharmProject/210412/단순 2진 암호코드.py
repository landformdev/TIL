import sys
sys.stdin = open('단순2진 암호코드_input.txt', 'r')

for tc in range(1, int(input())+1):

    N, M = map(int, input().split())

    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == 1:
                password = arr[i][0:j]

    print(password)