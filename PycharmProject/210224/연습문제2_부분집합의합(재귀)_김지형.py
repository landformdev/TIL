N = 10

sel = [0] * N


def powerset(idx):
    if idx == N:
        subset = []
        for k in range(1, 11):
            if sel[k - 1] == 1:
                subset.append(k)

        if sum(subset) == 10:
            print(subset)

        return

    for i in range(2):
        sel[idx] = i
        powerset(idx + 1)


powerset(0)
