import sys

sys.stdin = open('flatten_input.txt', 'r')

def BubbleSort(x):
    for i in range(len(x)-1, 0 , -1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

for tc in range(1, 11):
    dump = int(input())
    boxs = list(map(int, input().split()))
    ans = 0

    for do in range(dump):
        BubbleSort(boxs)
        if abs(boxs[-1] - boxs[0]) <= 1:
            ans = abs(boxs[-1] - boxs[0])
            break
        else:
            boxs[-1] -= 1
            boxs[0] += 1

    BubbleSort(boxs)
    ans = boxs[-1] - boxs[0]

    print('#{} {}'.format(tc, ans))
