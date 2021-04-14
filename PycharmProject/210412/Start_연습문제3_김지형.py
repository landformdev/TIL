# 입력 0269FAC9A0

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

code = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

check = ''
cnt = 0
i = 0
print(num)
while len(num) > i:
    check += num[i]
    i += 1
    cnt += 1
    if cnt == 6:
        if check in code:
            print(code.index(check))
            check = ''
        else:
            i -= 5
            check = ''
        cnt = 0
