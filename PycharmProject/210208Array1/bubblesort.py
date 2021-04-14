arr = [55, 7, 78, 12, 12]

def BubbleSort(a):
    for i in range(len(a)-1, 0 , -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

BubbleSort(arr)
print(arr)
