# import sys
# sys.stdin = open('피자_input.txt', 'r')

#수업 보고 함
#혼자서 다시 풀어볼 것

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    oven = []

    for i in range(N):
        oven.append((i+1, pizza[i]))

    next_pizza = N
    last_pizza = -1

    while oven:
        num, cheese = oven.pop(0)

        cheese = cheese//2
        last_pizza = num

        if cheese:
            oven.append((num, cheese))
        else:
            if next_pizza < M:
                oven.append((next_pizza+1, pizza[next_pizza]))

                next_pizza+=1

    print('#{} {}'.format(tc, last_pizza))