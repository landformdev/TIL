import sys
sys.stdin = open('회전_input.txt', 'r')

for tc in range(1, int(input())+1):

    N, M = map(int, input().split())

    Q = list(map(int, input().split()))

    nam = M % N

    for i in range(nam):
        tmp = Q.pop(0)
        Q.append(tmp)

    print('#{} {}'.format(tc, Q[0]))