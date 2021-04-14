import sys

sys.stdin = open('string_input.txt', 'r', encoding='utf-8')


def pattern_sum(p, t):
    i = 0
    j = 0
    cnt = 0
    while j < len(t):
        if p[i] != t[j]:
            j = j - i
            i = -1
        j += 1
        i += 1
        if i == len(p):
            j = j - i
            i = -1
            cnt += 1
    return cnt


for tc in range(1, 11):
    tc = int(input())
    pattern = input()
    text = input()

    ans = pattern_sum(pattern, text)

    print('#{} {}'.format(tc, ans))
