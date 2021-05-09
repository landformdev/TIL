def solution(s):
    eng_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    temp = ''
    answer = ''
    for i in s:
        if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            temp += i
            if temp in eng_num:
                j = str(eng_num.index(temp))
                answer += j
                temp = ''
        else:
            answer += i

    return int(answer)


print(solution('one4seveneight'))
