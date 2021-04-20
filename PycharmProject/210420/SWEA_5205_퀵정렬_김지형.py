# Lomuto partition
# 어렵다 차근차근 생각해보기
def lomuto(lst, low, high):
    if low < high:
        pivot = lst[high]
        left = low
        for right in range(low, high):
            if lst[right] <= pivot:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1

        # print(left, high, low)
        # print(lst)
        lst[left], lst[high] = lst[high], lst[left]

        lomuto(lst, low, left - 1)
        lomuto(lst, left + 1, high)

    return lst


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    A = lomuto(arr, 0, len(arr) - 1)
    # print(A)
    print('#{} {}'.format(tc, A[N // 2]))

# 1
# 11
# 1 6 2 7 56 2 4 6 1 19 1
