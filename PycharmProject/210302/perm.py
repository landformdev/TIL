arr = [1, 2, 3]


def perm(idx):
    if idx == N:
        lst = arr[:]
        result.append(lst)

    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx + 1)
            arr[idx], arr[i] = arr[i], arr[idx]


N = 3

result = []
perm(0)

print(result)