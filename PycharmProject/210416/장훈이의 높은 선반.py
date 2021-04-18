def combination(idx, sidx):
    if sidx == i:
        com = sel[:]
        temp.append(com)
        return
    if idx == N:
        return

    sel[sidx] = hobbits[idx]
    combination(idx + 1, sidx + 1)
    combination(idx + 1, sidx)


for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    hobbits = list(map(int, input().split()))

    temp = []
    res = 999999999
    for i in range(1, N + 1):
        sel = [0] * i
        combination(0, 0)

    for t in temp:
        if sum(t) >= B:
            if sum(t) < res:
                res = sum(t)
    print("#{} {}".format(tc, res - B))
