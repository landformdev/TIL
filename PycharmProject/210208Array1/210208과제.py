
# for i in range(1, 11):
#     result = 0
#     sol = 0
#     N = int(input())
#     B = list(map(int, input().split()))
#     for n in range(2, N - 2):
#         if B[n] >= B[n - 2] and B[n] >= B[n - 1] and B[n] >= B[n + 1] and B[n] >= B[n + 2]:
#             a = B[n - 2:n + 3]
#             for k in range(4, 0, -1):
#                 for j in range(k):
#                     if a[j] > a[j + 1]:
#                         a[j], a[j + 1] = a[j + 1], a[j]
#             sol = a[4] - a[3]
#
#             result += sol
#
#     print('#{} {}'.format(i, result))

def my_max(a, b):
    if a > b:
        return a
    return b

for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))

    ans = 0

    for idx in range(2, N-2):
        max_h = my_max(my_max(building[idx-2], building[idx-1]), my_max(building[idx+1], building[idx+2]))

        if building[idx] > max_h:
            ans += building[idx] - max_h




