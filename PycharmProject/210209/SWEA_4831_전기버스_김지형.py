import sys

sys.stdin = open('전기버스_input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    #K 최대 이동가능 수
    #N 종점
    #M 충전기 설치된 정류장 수
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    step = 0  # 이동거리
    cnt = 0  # 이동 횟수
    for m in range(M):  # 충전기 갯수보다 많이 이동하진 않을 것이므로
        for k in range(K, -1, -1):  # 최대거리로 이동한 후 한개씩 줄이며 충전소를 찾음
            if k == 0:  # 충전소를 못찾으면 break
                cnt = 0
                break

            elif step + k in arr:  # 충전소를 찾으면 이동거리에 추가되고 휫수 1증가
                step += k
                cnt += 1
                break

            elif step + k >= N:  # 종점보다 크거나같으면 break
                break

        if step >= N or k == 0:  # 이동거리가 종점보다 크거나같거나 충전소를 찾지 못했으면  -끝-
            break
    print('#{} {}'.format(tc, cnt))


    ###############################################################

    bus_stop = [0] * (N+1)

    for i in arr:
        bus_stop[i] = 1
    bus = 0  #버스위치
    ans = 0  #충전 횟수

    while True:
        #버스가 이동할 수 있는 만큼 이동을 하자
        bus += K
        if  bus >= N: break # 종점에 도착하거나 더 나아간 경우

        for i in range(bus, bus-K, -1):
            if bus_stop[i]:
                ans += 1
                bus = i
                break

        #충전기를 못찾았을때
        else:
            ans = 0
            break


########################################################################

    ans = 0

    charge = [0] + arr + [N]

    last = 0

    for i in range(1, M+2):  # 앞뒤로 두칸을 늘려 놨으므로
        if charge[i] - charge[i-1] > K:
            ans = 0
            break

        if charge[i] > last + K:
            last = charge[i-1]
            ans += 1


