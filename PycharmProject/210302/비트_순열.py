arr = [1, 2, 3]

N = 3

sel = [0] * N


def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        if check & (1 << j): continue

        sel[idx] = arr[j]
        perm(idx + 1, check | (1 << j))  # 썻다는걸 알기위해 합집합 사용

perm(0, 0)
