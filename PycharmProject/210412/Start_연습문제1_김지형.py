# 입력 0000000111100000011000000111100110000110000111100111100111111001100111



num = list(map(int, input()))
lst=[]
k = 0
ten = 0
cnt = 0
for i in num:
    lst.append(i)
    cnt += 1
    if cnt == 7:
        cnt = 0
        for j in range(len(lst)-1, -1, -1):
            ten += (lst[j] * (2**k))
            k += 1
            if k == len(lst):
                k = 0
                print(ten)
                ten = 0
        lst = []