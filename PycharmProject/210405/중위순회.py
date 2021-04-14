import sys
sys.stdin = open('중위순회_input.txt', 'r')


for tc in range(1, 11):
    word = []
    pair = []
    def inorder(n):
        if n > 0:
            inorder(left[n])
            word.append(n)
            inorder(right[n])
        return word

    V = int(input())
    E = V - 1

    left = [0]*(V+1)
    right = [0]*(V+1)
    pa = [0]*(V+1)

    for _ in range(V):
        tree = list(input().split())
        if len(tree) == 4:
            left[int(tree[0])] = int(tree[2])
            right[int(tree[0])] = int(tree[3])
            pa[int(tree[2])] = int(tree[0])
            pa[int(tree[3])] = int(tree[0])
            pair.append(tree[1])
        elif len(tree) == 3:
            left[int(tree[0])] = int(tree[2])
            pa[int(tree[2])] = int(tree[0])
            pair.append(tree[1])
        else:
            pair.append(tree[1])

    #root 구할 때
    root = 0
    for i in range(1, V+1):
        if pa[i] == 0:
            root = i
            break

    print('#{} '.format(tc), end='')
    inorder(root)
    for i in word:
        print(pair[i-1], end='')
    print()