# import sys
# sys.stdin = open('글자수_input.txt', 'r')

for tc in range(1, int(input())+1):
    chars = input()
    strings = input()

    # chars로 0의 value를 가진 딕셔너리 생성
    dict_char = {}
    for char in chars:
        dict_char[char] = 0

    # 비교를 위한 max_value 생성
    max_value = 0
    # strings를 돌리면서 dict_char의 key값과 같으면 +1
    for string in strings:
        for dc in dict_char:
            if string == dc:
                dict_char[string] += 1

                # max_value와 비교하며 갱신해 max 구현
                if max_value < dict_char[string]:
                    max_value = dict_char[string]


    print('#{} {}'.format(tc, max_value))
