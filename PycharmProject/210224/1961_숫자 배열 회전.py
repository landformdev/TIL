import sys
sys.stdin = open('숫자배열회전_input.txt', 'r')

def spin(x):
    map_90 = [[]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            map_90[i][j] = x[i][j]

    return map_90

for tc in range(1, int(input())+1):

    N = int(input())
    my_map = [list(map(int, input().split())) for _ in range(N)]


    print(spin(my_map))

