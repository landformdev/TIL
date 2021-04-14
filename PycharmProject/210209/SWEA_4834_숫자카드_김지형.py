test_case = int(input())

def BubbleSort(a):
    for i in range(len(a)-1, 0 , -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

for tc in range(test_case):
    N = int(input())
    arr = map(int, list(input()))
    lst = [0]*10
    lst2 = [0]*10

    for num in arr:
        lst[num] += 1
        lst2[num] += 1

    max_count = BubbleSort(lst)[-1]

    for idx in range(9, -1, -1):
        if max_count == lst2[idx]:
            break

    print('#{} {} {}'.format(tc+1, idx, max_count))

#################################################################

    N = int(input())
    card = input()

    count = [0] * 10

    max_count = -1
    max_num = -1

    for i in card:
        count[int(i)] += 1

    for i in range(len(count)):
        if max_count <= count[i]:
            max_num = i
            max_count = count[i]

    print('#{} {} {}'.format(tc + 1, max_num, max_count))
