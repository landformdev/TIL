def itoa(x):
    if x > 0:
        new = ''
        while x / 10 > 0:
            new += chr(48 + (x % 10))
            x = x // 10

        result = ''
        for i in range(len(new) - 1, -1, -1):
            result += new[i]
        return result

    elif x < 0:
        x = -x
        new = ''
        while x / 10 > 0:
            new += chr(48 + (x % 10))
            x = x // 10

        result = '-'
        for i in range(len(new) - 1, -1, -1):
            result += new[i]
        return result

    else:
        return chr(48)


print(itoa(1230))
print(itoa(-1241))
print(itoa(0))