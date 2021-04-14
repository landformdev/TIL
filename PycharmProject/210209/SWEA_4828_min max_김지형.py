test_case = int(input())

for tc in range(test_case):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print('#{} {}'.format(tc + 1, arr[-1] - arr[0]))



#################### for로 풀기#######################

max_value = 0
min_value = 987654321

for i in range(N):
    #최대값 계산
    if max_value < number[i]:
        max_value = number[i]
    #최소값 계산
    if min_value > number[i]:
        min_value = number[i]

