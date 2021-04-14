import sys

sys.stdin = open('두개의숫자열_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A

    max_value = 0

    for i in range(M-N+1):
        tmp = 0
        for j in range(N):
            tmp += A[j] * B[i+j]
        if max_value < tmp:
            max_value = tmp

    print('#{} {}'.format(tc, max_value))
