lst = [1, 10, 5, 8, 9, 3, 4, 7, 2, 6]


def quicksort(data):
    if start >= end:
        return data
    start = data[0]
    end = data[len(data)]
    key = start
    i = start + 1
    j = end


    ile i <= j:
        while i<= end and data[i] <= data[key]:
            i += 1
        while j > start and data[j] >= data[key]:
            j -= 1

        if i > j:
            data[j], data[key] = data[key], data[j]
        else:
            data[j], data[i] = data[i], data[j]

    return quicksort(data, start, j - 1), quicksort(data, j + 1, end)

print(quicksort(lst, 0, 9))