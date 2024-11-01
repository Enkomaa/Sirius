s = input()
s = s.split(' ')
stack = []
for i in s:
    if i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(a-b)
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(a // b)
    else:
        stack.append(int(i))
print(stack[0])
