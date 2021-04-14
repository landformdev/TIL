def perm(idx):

    if idx == N:
        print(sel)
        return

    for i in range(N):
        if check[i] == 0:
            sel[idx] = numbers[i]
            check[i] = 1
            perm(idx + 1)
            check[i] = 0  # 다음 반복을 위한 원상복구


N = 3
sel = [0]*N
check = [0]*N
numbers = []

for num in range(1, N+1):
    numbers.append(num)

perm(0)
