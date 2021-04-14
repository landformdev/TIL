# 입력 01D06079861D79F99F
sixteen = list(input())

num = ''
for x in sixteen:
    if x == '0':
        num += '0000'
    elif x == '1':
        num += '0001'
    elif x == '2':
        num += '0010'
    elif x == '3':
        num += '0011'
    elif x == '4':
        num += '0100'
    elif x == '5':
        num += '0101'
    elif x == '6':
        num += '0110'
    elif x == '7':
        num += '0111'
    elif x == '8':
        num += '1000'
    elif x == '9':
        num += '1001'
    elif x == 'A':
        num += '1010'
    elif x == 'B':
        num += '1011'
    elif x == 'C':
        num += '1100'
    elif x == 'D':
        num += '1101'
    elif x == 'E':
        num += '1110'
    elif x == 'F':
        num += '1111'

nums = list(map(int, num))

print(nums)
lst=[]
k = 0
ten = 0
cnt = 0
for i in nums:
    lst.append(i)
    cnt += 1
    # 7개 씩 끊기
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
# 끊고 남은 나머지
for j in range(len(lst)-1, -1, -1):
    ten += (lst[j] * (2**k))
    k += 1
    if k == len(lst):
        print(ten)

