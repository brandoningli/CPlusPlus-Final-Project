#Polish Notation Calculator for C++ Final Project Spring 2017

#A lesson in input, math, str.split(), substrings, etc.

#We will take input from the user in Polish Notation
#Numbers must start with a #
#For simplicity, we will assume all input has two numbers before any math operation

#Variable for user response to "Another Equation?"

cont = 'y'

#While the user wants to keep inputting equations...
while cont == 'y' or cont == 'Y':
    #get the input
    ipt = input("Enter an equation in Polish Notation. Put a \"#\" in front of numbers: ")

    #split the input into a list so each term is an element
    terms = ipt.split()

    #initialize a list to act as a stack
    stack = []

    #the append() method of a list puts an element at the end
    #the pop() method with no parameters takes the element at the end
    #so we can still use the FILO principle

    #For each term...
    for t in terms:
        #If the first char is a #, then it's a number...
        if t[0] == '#':
            #add the number to the stack as a float.
            #SUBSTRING NOTATION IN PYTHON:
            # str[1:4] is equivalent to str.substring(1,4) in C++ or Java
            # str[1:] gets the substring from index 1 to the end. Like str.substring(1)
            # str[:5] gets the substring from index 0 to 5. It's just shorthand.
            stack.append(float(t[1:]))
        #If it's one of the math symbols, do it!
        elif t[0] == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif t[0] == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif t[0] == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif t[0] == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
        elif t[0] == '^':
            a = stack.pop()
            b = stack.pop()
            #In python, you do exponents with the ** operator
            stack.append(b**a)
        elif i[0] == '=':
            break
    #After we go through all the terms, the answer is on the top of the stack
    print("The answer is " + str(stack.pop()))

    #Ask the user if they want to input another one...
    ipt2 = input("Another Equation? Yes/No: ")

    #For our loop, cont needs to be the first character of that input
    cont = ipt2[0]

    stack.clear()
