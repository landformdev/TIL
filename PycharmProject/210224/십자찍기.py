my_map = [[0] * 10 for _ in range(10)]

my_map[4][6] = 8

r = [-1, 1, 0, 0]
c = [0, 0, -1, 1]

for i in range(10):
    for j in range(10):
        if my_map[i][j] == 8:
            for n in range(4):
                for l in range(1, 8):
                    if 0 <= i + r[n] * l < 10 and 0 <= j + c[n] * l < 10:
                        my_map[i + r[n] * l][j + c[n] * l] = 4
                    else:
                        continue

for k in range(10):
    print(my_map[k])


