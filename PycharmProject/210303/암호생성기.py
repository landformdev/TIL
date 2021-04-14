import sys
sys.stdin = open('암호생성기_input.txt', 'r')

for _ in range(10):
    tc = int(input())
    Q = list(map(int, input().split()))
    num = 999  # 아무값
    cnt = 0  # 빼기위해서 1씩 증가할 값

    while True:
        num = Q.pop(0)  # 젤앞을 빼서
        cnt += 1
        num -= cnt  # cnt만큼 감소

        # 한주기가 5니까
        if cnt == 5:
            cnt = 0
        # 값이 0보다 작거나 같아질 경우 종료
        if num <= 0:
            num = 0
            Q.append(num)
            break
        # 삽입
        Q.append(num)

    print('#{} {}'.format(tc, ' '.join(map(str, Q))))
