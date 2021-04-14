def reverse1(x):
    new = ''
    for i in range(len(x) - 1, -1, -1):
        new += x[i]
    return new


print(reverse1('abcd'))


def reverse2(x):
    new_list = list(x)
    for i in range(len(x) // 2):
        new_list[i], new_list[len(x) - 1 - i] = new_list[len(x) - 1 - i], new_list[i]

    return ''.join(new_list)


print(reverse2('qwer'))
