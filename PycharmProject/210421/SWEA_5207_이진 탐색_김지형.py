for tc in range(1, int(input())+1):

    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    l = A[0]
    r = A[-1]
    m = A[N//2]

    for i in B:
