
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(n):
    if n > 0:
        print(n, end=' ')
        preorder(left[n])
        preorder(right[n])


V = int(input())
tree = list(map(int, input().split()))

E = V-1

left = [0]*(V+1)
right = [0]*(V+1)
pa = [0]*(V+1)


for i in range(E):
    pn, cn = tree[i*2], tree[i*2+1]

    if left[pn] == 0:
        left[pn] = cn
    else:
        right[pn] = cn

    pa[cn] = pn

#root 구할 때
root = 0
for i in range(1, V+1):
    if pa[i] == 0:
        root = i
        break


preorder(root)