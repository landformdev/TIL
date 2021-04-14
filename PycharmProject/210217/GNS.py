import sys
sys.stdin = open('GNS_input.txt', 'r')

def change(x):
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(len(num_list)):
        if x == num_list[i]:
            return i

def reverse_change(x):
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(len(num_list)):
        if x == i:
            return num_list[i]

for tc in range(1, int(input())+1):
    N = int(list(input().split())[1])

    lst = list(map(change, input().split()))

    for i in range(N-1):
        min = i
        for j in range(i+1, N):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]

    lst = list(map(reverse_change, lst))

    print('#{}\n{}'.format(tc, ' '.join(map(str, lst))))


