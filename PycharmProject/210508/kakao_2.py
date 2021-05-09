def solution(places):
    answer = [1] * len(places)
    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]

    def dfs(r, c, distance, visit):

        visit[r][c] = 1
        distance += 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                continue
            if places[tc][nr][nc] == 'P':
                if distance < 2:
                    answer[tc] = 0
                    return
                else:
                    return

            if places[tc][nr][nc] == 'X':
                continue
            if visit[nr][nc] == 1:
                continue
            if distance >= 2:
                continue

            dfs(nr, nc, distance, visit)

    for tc in range(len(places)):

        for i in range(5):
            for j in range(5):
                if places[tc][i][j] == 'P':
                    visited = [[0] * 5 for _ in range(5)]
                    dfs(i, j, 0, visited)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# 테스트 케이스 6개 실패