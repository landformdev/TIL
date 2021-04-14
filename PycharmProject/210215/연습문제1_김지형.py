nums = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]


def absol(x):
    if x < 0:
        return -x
    return x


abs_sum = []
ans = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for i in range(5):
    for j in range(5):
        result = 0
        for k in range(4):
            if 0 < (i + dr[k]) and 0 < (j + dc[k]) and 5 > (i + dr[k]) and 5 > (j + dc[k]):
                result += absol(nums[i + dr[k]][j + dc[k]] - nums[i][j])
        abs_sum.append(result)

for sums in abs_sum:
    ans += sums

print(ans)
