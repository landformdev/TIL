# import sys
#
# sys.stdin = open('연습문제3_input.txt', 'r')

V, E = map(int, input().split())

arr_map = [[0] * (V + 1) for _ in range(V + 1)]


def DFS(v):
    check[v] = True
    print(v, end=' ')

    for w in range(1, V + 1):
        if arr_map[v][w] and check[w] != 1:
            DFS(w)


for _ in range(E):
    i, j = map(int, input().split())
    arr_map[i][j] = 1
    arr_map[j][i] = 1

check = [False] * (V + 1)

DFS(1)
