arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = len(arr)
lst = []
ans = []

################################################

for i in range(1 << n):
    lst.append([])
    for j in range(n):
        if i & (1 << j):
            lst[i].append(arr[j])
print(lst)

################################################

# for i in range(1 << n):
#     lst.append([])
#     for j in range(n):
#         if i & (1 << j):
#             lst[i].append(j+1)
# print(lst)

################################################

for k in lst:
    sum_num = 0
    for l in k:
        sum_num += l
    if sum_num == 10:
        ans.append(k)

print(ans)
