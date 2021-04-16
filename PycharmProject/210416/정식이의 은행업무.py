# 1
# 1010
# 212

for tc in range(1, int(input()) + 1):
    error_bin = input()
    error_ternary = input()

    bin_num = 0
    ter_num = 0

    for n in range(len(error_bin)):
        bin_num += int(error_bin[::-1][n]) * (2 ** n)

    # print(bin_num)

    for m in range(len(error_ternary)):
        ter_num += int(error_ternary[::-1][m]) * (3 ** m)

    # print(ter_num)

    print('#{}'.format(tc), end=" ")

    for i in range(len(error_bin)):
        result = 0

        if int(error_bin[::-1][i]) == 1:
            result = bin_num - 2 ** i

        elif int(error_bin[::-1][i]) == 0:
            result = bin_num + 2 ** i

        for j in range(len(error_ternary)):

            if int(error_ternary[::-1][j]) == 0:
                if result == ter_num + 3 ** j:
                    print(result)
                elif result == ter_num + (3 ** j) * 2:
                    print(result)

            elif int(error_ternary[::-1][j]) == 1:
                if result == ter_num + 3 ** j:
                    print(result)
                elif result == ter_num - 3 ** j:
                    print(result)

            elif int(error_ternary[::-1][j]) == 2:
                if result == ter_num - 3 ** j:
                    print(result)
                elif result == ter_num - (3 ** j) * 2:
                    print(result)
