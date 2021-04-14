# 으ㅏㅏㅏㅏㅏㅏㅏ 너무 헷갈린다.

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]


def bfs(v):
    Q = [v]
    visited = [v]

    while Q:
        n = Q.pop(0)

        for i in range(1, N):
            if i not in visited and G[n][i]:
                Q.append(i)
                visited.append(i)

    return visited


N = 8

G = [[0] * N for _ in range(N)]

for i in range(0, len(lst), 2):
    G[lst[i]][lst[i + 1]] = 1
    G[lst[i + 1]][lst[i]] = 1

    print(bfs(1))

for row in G:
    print(*row)
