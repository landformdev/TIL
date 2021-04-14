import sys

sys.stdin = open('부분집합의합_input.txt', 'r')


def sum_all(numbers):
    result = 0
    for num in numbers:
        result += num
    return result


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    arrs = []
    for i in range(1 << 12):
        arrs.append([])
        for j in range(12):
            if i & (1 << j):
                arrs[i].append(A[j])
    print(arrs)

    cnt = 0
    for arr in arrs:
        if len(arr) == N and sum_all(arr) == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
