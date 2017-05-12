cont = 'y'

while cont == 'y' or cont == 'Y':
    ipt = input("Enter an equation in Polish Notation. Put a \"#\" in front of numbers: ")

    terms = ipt.split()

    stack = []

    for i in terms:
        if i[0] == '#':
            stack.append(float(i[1:]))
        elif i[0] == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif i[0] == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i[0] == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif i[0] == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
        elif i[0] == '^':
            a = stack.pop()
            b = stack.pop()
            stack.append(b**a)
        elif i[0] == '=':
            break
    print("The answer is " + str(stack.pop()))

    ipt2 = input("Another Equation? Yes or no? ")
    cont=ipt2[0]

    stack.clear()
