# import sys
# sys.stdin = open('문자열비교_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    string = input()
    main_string = input()

    # 고지식한 패턴매칭 알고리즘을 써보자
    # 인덱스값 0으로 시작
    i = 0
    j = 0

    # 패턴을 찾거나 문장을 다 돌면 탈출
    while len(string) > i and len(main_string) > j:
        # 문장과 단어의 값이 같다면 반복진행
        # 값이 다르다면 i인덱스 초기화 & j인덱스를 진행한 i값만큼 감소
        if string[i] != main_string[j]:
            j = j - i
            i = -1
        j += 1
        i += 1

    print('#{}'.format(tc), end=' ')
    # 탈출 이유가 패턴을 찾아 i값이 단어의 길이와 같다면 1 아니면 0
    if i == len(string):
        print(1)
    else:
        print(0)
