# 5
# 4 0
# 4 30
# 4 47
# 5 31
# 5 62

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    result = ''

    for i in range(N):  # 뒤에서 N 자리만큼만 result에 저장
        result += '1' if M & (1<<i) else '0'

    print('#{}'.format(tc), end=' ')
    # result에 저장값이 모두 1이면 ON 아니면 OFF
    if '1'*N == result:
        print('ON')
    else:
        print('OFF')
