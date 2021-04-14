import sys

sys.stdin = open('삼성시의버스노선_input.txt', 'r')

for tc in range(1, int(input())+1):
    AB_list = []  # A~B까지 가는 버스들을 담을 리스트
    N = int(input())  # 버스 대수
    station = []
    for n in range(N):  # 버스 담기
        AB_list.append(list(map(int, input().split())))
    P = int(input())  # 버스정류장 갯수
    for p in range(P):
        station.append(int(input()))

    bus_station = [0] * 5000  # 정류장에 오는 버스를 카운트할 리스트를 만든다

    for k in range(N): # bus_station 리스트에 카운트
        for i in range(AB_list[k][0], AB_list[k][1]+1):
            bus_station[i-1] += 1

    print('#{} '.format(tc), end='')
    for l in station:
        print('{}'.format(bus_station[l-1]), end=' ')
    print()