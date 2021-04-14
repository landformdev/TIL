import sys

sys.stdin = open('영준이카드_input.txt', 'r')

for tc in range(1, int(input()) + 1):

    card_map = [[0] * 14 for _ in range(4)]

    cards = input()

    card_count = [13,13,13,13]

    error = 0

    for i in range(0, len(cards), 3):
        num = int(cards[i + 1] + cards[i + 2])

        if cards[i] == 'S':
            card_map[0][num] += 1
            if card_map[0][num] == 2:
                error = 1
            card_count[0] -= 1

        if cards[i] == 'D':
            card_map[1][num] += 1
            if card_map[1][num] == 2:
                error = 1
            card_count[1] -= 1

        if cards[i] == 'H':
            card_map[2][num] += 1
            if card_map[2][num] == 2:
                error = 1
            card_count[2] -= 1

        if cards[i] == 'C':
            card_map[3][num] += 1
            if card_map[3][num] == 2:
                error = 1
            card_count[3] -= 1


    print('#{}'.format(tc), end=' ')
    if error == 0:
        print(*card_count)
    else:
        print('ERROR')
