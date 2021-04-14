import sys

sys.stdin = open('그래프경로_input.txt', 'r')


def recursive_dfs(v):
    visited[v] = True
    ans.append(v)

    for w in range(1, V + 1):
        if visited[w] != 1 and V_map[v][w]:
            recursive_dfs(w)


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    V_map = [[0] * (V + 1) for _ in range(V + 1)]

    ans = []

    for n in range(E):
        i, j = map(int, input().split())
        V_map[i][j] = 1

    S, G = map(int, input().split())

    visited = [False] * (V + 1)

    recursive_dfs(S)

    print('#{}'.format(tc), end=' ')
    if G in ans:
        print(1)
    else:
        print(0)
