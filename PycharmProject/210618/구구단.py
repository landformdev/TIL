

s, e = map(int, input().split())

if s < 2 or s > 9 or e < 2 or e > 9:
    print("INPUT ERROR!")
    s, e = map(int, input().split())

if s > e:
    for i in range(1, 10):
        for num in range(s, e-1, -1):
            print('{} * {} = {}'.format(num, i, num*i), end='   ')
        print()
else:
    for i in range(1, 10):
        for num in range(s, e+1):
            print('{} * {} = {}'.format(num, i, num*i), end='   ')
        print()