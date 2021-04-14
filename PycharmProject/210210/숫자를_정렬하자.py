import sys

sys.stdin = open('숫자정렬_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print('#{} '.format(tc), end='')
    for num in nums:
        print(num, end=' ')
    print()