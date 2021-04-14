import sys

sys.stdin = open('현주_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, Q = map(int, input().split())

    boxs = [0]*N

    for i in range(1, Q+1):
        idx = list(map(int, input().split()))
        for j in range(idx[0], idx[1]+1):
            boxs[j-1] = i

    print('#{} {}'.format(tc, ' '.join(map(str, boxs))))
