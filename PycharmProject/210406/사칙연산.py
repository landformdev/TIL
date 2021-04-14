for tc in range(1, 11):

    def oper(n):
        if n > 0:
            oper(left[n])
            oper(right[n])
            if tree[n] == '+':
                tree[n] = int(tree[left[n]]) + int(tree[right[n]])
            elif tree[n] == '-':
                tree[n] = int(tree[left[n]]) - int(tree[right[n]])
            elif tree[n] == '/':
                tree[n] = int(tree[left[n]]) / int(tree[right[n]])
            elif tree[n] == '*':
                tree[n] = int(tree[left[n]]) * int(tree[right[n]])


    V = int(input())
    left = [0]*(V+1)
    right = [0]*(V+1)

    tree = [0]
    for _ in range(V):
        x = list(input().split())
        if len(x) == 4:
            tree.append(x[1])
            left[int(x[0])] = int(x[2])
            right[int(x[0])] = int(x[3])
        else:
            tree.append(x[1])

    oper(1)
    print('#{} {}'.format(tc, int(tree[1])))
