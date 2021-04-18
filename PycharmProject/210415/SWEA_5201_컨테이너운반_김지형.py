def badal(n, m):
    v = [0] * n
    s = 0
    for i in range(m):
        for j in range(n):
            if v[j] == 0 and trucks[i] >= weights[j]:
                s += weights[j]
                v[j] = 1
                break

    return s


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 컨테이너 수, 트럭 수

    weights = list(map(int, input().split()))  # 화물무게
    trucks = list(map(int, input().split()))  # 적재용량
    weights = sorted(weights, reverse=True)
    trucks = sorted(trucks, reverse=True)

    result = badal(N, M)

    print('#{} {}'.format(tc, result))
