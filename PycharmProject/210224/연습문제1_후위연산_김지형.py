input = '5+(7+4/2*(5-4+5)*1/2+1)'

operator = ['+', '-', '*', '/', '(', ')']

stack = ['X']

result = []

for i in input:
    if i not in operator:
        result.append(i)

    elif i == '(':
        stack.append(i)

    elif i == ')':
        while stack[len(stack) - 1] != '(':
            result.append(stack.pop())
        stack.pop()

    elif i == '+' or i == '-':
        while stack[len(stack) - 1] == '+' or stack[len(stack) - 1] == '-' or stack[len(stack) - 1] == '*' or stack[len(stack) - 1] == '/':
            result.append(stack.pop())
        stack.append(i)

    elif i == '*' or i == '/':
        while stack[len(stack) - 1] == '*' or stack[len(stack) - 1] == '/':
            result.append(stack.pop())
        stack.append(i)


while stack[len(stack) - 1] == '+' or stack[len(stack) - 1] == '-' or stack[len(stack) - 1] == '*' or stack[len(stack) - 1] == '/':
    result.append(stack.pop())

print(''.join(result))
