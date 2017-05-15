# Python Version of Dierker's Simplified War Program
# For C++ Class Final Project Spring 2017

# A few important things to note about Python:
# Indention matters. There's no {} for anything except a specific data structure.
# Use tab or two spaces, but keep it consistent

# Variables need not be declared before use, and can change type

# We'll talk about other things as we go.

#First we'll import some things we'll need later
from time import sleep
import random

#Let's write a class for a Card.

class Card:
    #Class variables are initialized here. They are like "static" Variables in Java, where they're the same for all objects of this type.
    #We don't have any for this class, so we'll continue.

    #Unlike Java or C++, you can only have ONE constructor.
    #It is names __init__(self) (that's two underscores on either side)
    #You must include self in every method in the class so that it has a reference to itself.
    #You can define other parameters for __init__.
    #Methods, including __init__, can also have default values.

    #Let's write the constructor and default to a 2 of hearts.
    #Hearts = chr(3), Diamonds = chr(4), Clubs = chr(5), Spades = chr(6)
    def __init__(self, type='2', suit=chr(3)):
        #Instance variables are unique to each object. You reference
        #them in the class with 'self' and the '.' operator.
        self.type = type
        self.suit = suit

        #Now, let's calculate the value of the Card
        #Python doesn't have switch statements for some reason. Werid, I know.
        #If statements in Python are like those in Java or C++, with four exceptions:
        #   1) Use the words 'and' and 'or' instead of the symbols
        #   2) Use a colon and indent instead of {}
        #   3) You only need () for order of operations stuff
        #   4) Use 'elif' instead of 'else if'

        if ord(self.type) <= 57:
             #ord() gets the ascii value of a character
            self.value = int(self.type)
        elif self.type == 'X':
            self.value = 10
        elif self.type == 'J':
            self.value = 11
        elif self.type == 'Q':
            self.value = 12
        elif self.type == 'K':
            self.value = 13
        elif self.type == 'A':
            self.value = 14
        else:
            self.value = 1

    #Now, let's define some methods for this Card
    #Remember to include 'self' as a parameter in Methods

    #We won't make accessors or modifiers, since all variables are Public.
    #We will make a modifier for type, though, because the value is dependant on it.
    def changeType(self, type):
        self.type = type
        if ord(self.type) <= 57:
            self.value = int(self.type)
        elif self.type == 'X':
            self.value = 10
        elif self.type == 'J':
            self.value = 11
        elif self.type == 'Q':
            self.value = 12
        elif self.type == 'K':
            self.value = 13
        elif self.type == 'A':
            self.value = 14
        else:
            self.value = 1

    #Change the string representation of the class
    #This is like a toString() method in Java or overloading << in C++
    def __str__(self):
        return "|" + self.type + " " + self.suit + "|"

#Global Variables

#We'll use a list to act as a "deck"
#Lists use [] to initialize. Weird that's not an array, right?
#Lists also have a few useful functions we'll use later that make them more convenient than arrays.
deck=[]
computer=[]
player=[]

playerScore = 0
computerScore = 0

#We don't need a main function, but we'll make on to make things easier for us later
def main():
    initializeDeck()
    printDeck(deck)
    shuffle()
    printDeck(deck)
    deal()
    print("PLR: ")
    printDeck(player)
    print("CPU: ")
    printDeck(computer)
    play()
    playAgain()


#Initialie deck, not exactly in order
def initializeDeck():
    #For-loops in Python can be a bit weird. Take a look.
    for i in range(2,10):
        #This is equivalent to for(int i = 2, i < 10; i++) in C++/Java
        for j in range(3,7):
            #Nested LooplayerScore!
            #Add the number cards to the deck
            deck.append(Card(str(i), chr(j)))
    #and now for the other special cards
    for i in range(3,7):
        deck.append(Card('X', chr(i)))
        deck.append(Card('J', chr(i)))
        deck.append(Card('Q', chr(i)))
        deck.append(Card('K', chr(i)))
        deck.append(Card('A', chr(i)))

#Print out a deck of cards
def printDeck(deck):
    #We're referencing a local variable 'deck' here
    for c in deck:
        print(c, end='')
    print() #Ends the line

#Let's make sure it can create ok...
#add initializeDeck() and printDeck(deck) to main()


#let's shuffle the deck
def shuffle():
    #Now we'll use the global variable 'deck'
    global deck
    temp = deck.copy() #Copies the deck to a temporary list
    deck.clear() #Clears the deck
    while len(temp) > 0:
        #RANDOM NUMBERS:
        #We don't need to seed it; It'll do that for us!
        #random.randint(a,b) gets a random integer such that a <= N <= B
        idx = random.randint(0, len(temp)-1)

        #Lists have a pop function like stacks/queues do in C++
        #However, this one can pop ANY INDEX YOU WANT and actually returns the object you're popping!
        deck.append(temp.pop(idx))

#And now let's check if it shuffles correctly...
#add shuffle() and printDeck(deck) to main()

#Let's deal the deck out to the players...
def deal():
    global computer
    global player
    global deck
    while len(deck) > 0:
        computer.append(deck.pop())
        player.append(deck.pop())

#And putting that in action...
#add deal() and print PLR and CPU decks to main()


#Let's write the game itself
def play():
    global playerScore
    global computerScore

    while len(player) > 0 and len(computer) > 0:
        print("----------")
        input("Press Enter to Draw Cards...") #this reads input, but we're not storing it.
        print("----------")

        plrCard = player.pop()
        cpuCard = computer.pop()

        print("You   Drew: " + str(plrCard))
        print("Comp. Drew: " + str(cpuCard))

        if plrCard.value > cpuCard.value:
            print("You Won!")
            #There's no ++ or -- in Python. Weird, right?
            playerScore += 1
        elif cpuCard.value > plrCard.value:
            print("Computer Won...")
            computerScore += 1
        else:
            print("Tie!")

    #End the game
    print("----------")
    print("Final Score:")
    #Even though Python prints integers fine, there's already a string, and we can't add an int to a string! So we need to convert it.
    print("CPU: " + str(computerScore))
    print("You: " + str(playerScore))

    if playerScore > computerScore:
        print("You Won the Game!")
    elif computerScore > playerScore:
        print("The Computer Won the Game!")
    else:
        print("It's a Tie!")

#Ask the user if they want to play again...
def playAgain():
    global playerScore
    global computerScore
    ipt = ""
    while len(ipt) == 0:
        ipt = input("Want to play again? Yes or [No]: ") #reads a line of input as string
    #We really only want to look at the first character
    iptChar = ipt[0]

    #Side note: substrings use a similar notation, but with a colon
    #i.e. C++'s str.substring(5)  -> Python  str[5:]
    # C++'s str.substring(2,6) -> Python str[2:6]

    if iptChar == 'y' or iptChar == 'Y':
        playerScore=0
        computerScore=0
        main()

#Call the Game and playAgain()
#add play() and playAgain() to main()

#Call main() to start everything
main()
