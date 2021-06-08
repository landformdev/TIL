def bfs(dist_count, fuel, idx):
    global minimum
    if fuel < 0 or idx >= N:  # 연료가 0보다 작거나 범위 벗어난 경우
        return

    if is_station[idx]:  # 주유소이면
        fuel = min(M, fuel + locations[idx])
    else:
        if locations[idx]:  # 트랩이면
            fuel = fuel // 2

    if idx == N - 1:  # 도착했을 경우
        if minimum > (M - fuel) * dist_count:
            minimum = (M - fuel) * dist_count
    else:
        if fuel > 0:  # 연료가 남아있으면
            bfs(dist_count+1, fuel-1, idx+1)
            bfs(dist_count+1, fuel-2, idx+2)
            bfs(dist_count+1, fuel-3, idx+3)


for tc in range(int(input())):
    N, M = map(int, input().split())
    S = input()
    minimum = 100000
    is_station = [0] * N
    locations = []
    idx = 0
    for s in S:
        if s != '+':
            locations.append(int(s))
            idx += 1
        else:
            is_station[idx] = 1
    bfs(0, M, 0)
    if minimum == 100000:
        print(f'{tc+1} -1')
    else:
        print(f'{tc+1} {minimum}')