for tc in range(1, int(input()) + 1):

    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0] * (N + 1)
    i = 1
    for num in nums:
        heap[i] = num
        if i > 1:
            # root까지 다 정렬될 때까지 반복
            j = i
            while j > 1:
                if heap[j // 2] > heap[j]:
                    heap[j // 2], heap[j] = heap[j], heap[j // 2]
                j -= 1
        i += 1

    # 조상님 더하기
    result = 0
    while N > 0:
        N //= 2
        result += heap[N]

    print('#{} {}'.format(tc, result))
