import sys
sys.stdin = open('쇠막대기_input.txt', 'r')


def pattern(p, t):
    i = 0
    j = 0
    cnt = 0
    while j < len(t):
        if p[i] != t[j]:
            j = j-i
            i = -1
        j += 1
        i += 1
        if i == len(p):
            j = j-i
            i = -1
            cnt += 1
    return cnt

for tc in range(1, int(input())+1):

    iron = input()

    print(pattern(')(', iron))
    print('#{} {}'.format(tc, pattern('((', iron) + pattern('))', iron)))