#Polish Notation Calculator with File Input for C++ Final Project Spring 2017

#A lesson in file input

#We will take input from the user in Polish Notation
#Numbers must start with a #
#For simplicity, we will assume all input has two numbers before any math operation

#To get file input, we need to import it
import fileinput

#Initialize the fileinput
#You CAN input from multiple files. They will go back-to-back
filein = fileinput.input(files=('polish.txt'))

#Keep a counter of which equation we're working on
eqnum = 1

#We will go through each line in the file, one equation per line
for line in filein:
    
    #split the input line into a list so each term is an element
    terms = line.split()

    #-----This bit is the same as the other Polish Calculator-----

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
            
    #---This line is not the same----
    #After we go through all the terms, the answer is on the top of the stack
    print("The answer to equation " + str(eqnum) + " is " + str(stack.pop())) 
